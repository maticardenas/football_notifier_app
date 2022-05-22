from datetime import datetime

from django.db.models import Q
from notifier.models import Fixture, TeamStanding
from notifier.src.config.telegram_notif import FOOTBALL_TELEGRAM_RECIPIENTS
from notifier.src.emojis import Emojis
from notifier.src.senders.telegram_sender import send_telegram_message
from notifier.src.utils.date_utils import get_date_spanish_text_format
from notifier.src.utils.fixtures_utils import (get_image_search,
                                               get_next_fixture, get_last_fixture)
from notifier.src.utils.message_utils import get_team_intro_messages, get_highlights_text


class TeamFixturesManager:
    def __init__(self, season: str, team_id: str) -> None:
        self._season = season
        self._team_id = team_id

    def notify_next_fixture(self) -> None:
        team_fixtures = Fixture.objects.filter(
            Q(home_team__team_id=self._team_id) | Q(away_team__team_id=self._team_id),
            Q(season=self._season),
        )

        next_team_fixture = get_next_fixture(team_fixtures)

        if next_team_fixture:
            if next_team_fixture.remaining_time().days < 30:
                self._perform_fixture_notification(next_team_fixture)


    def notify_last_fixture(self) -> None:
        team_fixtures = Fixture.objects.filter(
            Q(home_team__team_id=self._team_id) | Q(away_team__team_id=self._team_id),
            Q(season=self._season),
        )

        last_team_fixture = get_last_fixture(
            team_fixtures, self._team_id
        )

        if last_team_fixture:
            team_standing = TeamStanding.objects.filter(
                Q(team__team_id=self._team_id),
                Q(season=self._season),
                Q(league__name=last_team_fixture.championship.name)
            )

            last_team_fixture.highlights = ""

            self._perform_last_fixture_notification(
                    last_team_fixture, team_standing
                )

            # if -1 <= last_team_fixture.remaining_time().days <= 0:
            #     # last_team_fixture.highlights = get_youtube_highlights_videos(
            #     #     last_team_fixture.home_team, last_team_fixture.away_team
            #     # )
            #     self._perform_last_fixture_notification(
            #         last_team_fixture, team_standing
            #     )
    #
    def _perform_last_fixture_notification(
        self, team_fixture: Fixture, team_standing: TeamStanding
    ) -> None:

        match_image_url = get_image_search(
            f"{team_fixture.home_team.name} vs {team_fixture.away_team.name}"
        )

        # telegram
        team_standing_msg = (
            f"{Emojis.RED_EXCLAMATION_MARK.value} Situación actual en el campeonato: \n\n{team_standing.telegram_like_repr()}\n"
            if team_standing
            else ""
        )
        intro_message = get_team_intro_messages(
            self._team_id, is_group_notification=True
        )["last_match"]
        highlights_text = get_highlights_text(team_fixture.highlights)

        for recipient in FOOTBALL_TELEGRAM_RECIPIENTS:
            telegram_message = (
                f"{Emojis.WAVING_HAND.value}Hola {recipient}!\n\n{intro_message} "
                f"jugó ayer! \nEste fue el resultado: \n\n{team_fixture.matched_played_telegram_like_repr()}"
                f"\n\n{team_standing_msg}\n{highlights_text}"
            )
            send_telegram_message(
                FOOTBALL_TELEGRAM_RECIPIENTS[recipient],
                telegram_message,
                match_image_url,
            )

        # email
        # intro_message = get_team_intro_messages(self._team_id)["last_match"]
        # team_standing_email_msg = (
        #     f"Situación actual en el campeonato: \n\n{
        #     team_standing.email_like_repr()}"
        #     if team_standing
        #     else ""
        # )
        # match_image_text = f"<img notifier.src='{match_image_url}'>"
        # email_standing_message = (
        #     f"{Emojis.RED_EXCLAMATION_MARK.value}{team_standing_email_msg}\n"
        # )
        # highlights_text = get_highlights_text(team_fixture.highlights,
        # email=True)

        # for recipient in EMAIL_RECIPIENTS:
        #     message = (
        #         f"{Emojis.WAVING_HAND.value}Hola {recipient}!\n\n{
        #         intro_message} "
        #         f"jugó ayer!<br /><br />{match_image_text}<br /><br />Este
        #         fue el resultado: \n\n{
        #         team_fixture.matched_played_email_like_repr()}"
        #         f"<br /><br />{email_standing_message}<br /><br />{
        #         highlights_text}"
        #     )
        #
        #     send_email_html(
        #         f"{team_fixture.home_team.name} ({
        #         team_fixture.match_score.home_score}) - "
        #         f"({team_fixture.match_score.away_score}) {
        #         team_fixture.away_team.name}",
        #         message,
        #         EMAIL_RECIPIENTS[recipient],
        #     )

    def _perform_fixture_notification(self, team_fixture: Fixture) -> None:
        spanish_format_date = get_date_spanish_text_format(team_fixture.bsas_date)
        match_image_url = get_image_search(
            f"{team_fixture.home_team.name} vs {team_fixture.away_team.name}"
        )
        match_image_text = f"<img width='100%' height='100%' src='{match_image_url}'>"
        date_text = (
            "es HOY!"
            if team_fixture.bsas_date.day == datetime.today().day
            else f"es el {Emojis.SPIRAL_CALENDAR.value} {spanish_format_date}."
        )

        # telegram
        for recipient in FOOTBALL_TELEGRAM_RECIPIENTS:
            intro_message = get_team_intro_messages(
                self._team_id, is_group_notification=True
            )["next_match"]
            telegram_message = f"{Emojis.WAVING_HAND.value}Hola {recipient}!\n\n{intro_message} {date_text}\n\n{team_fixture.telegram_like_repr()}"
            send_telegram_message(
                FOOTBALL_TELEGRAM_RECIPIENTS[recipient],
                telegram_message,
                photo=match_image_url,
            )

        # email
        # for recipient in EMAIL_RECIPIENTS:
        #     intro_message = get_team_intro_messages(self._team_id)[
        #     "next_match"]
        #     message = f"{Emojis.WAVING_HAND.value}Hola {recipient}!\n\n{
        #     intro_message} {date_text}\n\n<br /><br />{
        #     match_image_text}<br /><br />{team_fixture.email_like_repr()}"
        #     send_email_html(
        #         f"{team_fixture.home_team.name} vs. {
        #         team_fixture.away_team.name}",
        #         message,
        #         EMAIL_RECIPIENTS[recipient],
        #     )

    #
    # def _perform_line_up_confirmed_notification(self, team_fixture:
    # Fixture) -> None:
    #     match_teams = f"{team_fixture.home_team.name} vs {
    #     team_fixture.away_team.name}"
    #     match_image_url = get_image_search(match_teams)
    #     match_image_text = f"<img notifier.src='{match_image_url}'>"
    #
    #     # telegram
    #     for recipient in FOOTBALL_TELEGRAM_RECIPIENTS:
    #         intro_message = f"Se actualizó la alineación para {match_teams}:"
    #         telegram_message = f"{Emojis.WAVING_HAND.value}Hola {
    #         recipient}!\n\n{intro_message}\n\n{
    #         team_fixture.telegram_like_repr()}"
    #         send_telegram_message(
    #             FOOTBALL_TELEGRAM_RECIPIENTS[recipient], telegram_message,
    #             photo=match_image_url
    #         )
    #
    #     # email
    #     for recipient in EMAIL_RECIPIENTS:
    #         intro_message = get_team_intro_messages(self._team_id)[
    #         "next_match"]
    #         message = f"{Emojis.WAVING_HAND.value}Hola {recipient}!\n\n{
    #         intro_message}\n\n<br /><br />{match_image_text}<br /><br />{
    #         team_fixture.email_like_repr()}"
    #         send_email_html(
    #             f"{team_fixture.home_team.name} vs. {
    #             team_fixture.away_team.name}",
    #             message,
    #             EMAIL_RECIPIENTS[recipient],
    #         )

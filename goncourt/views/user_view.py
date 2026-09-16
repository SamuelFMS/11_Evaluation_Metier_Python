from business import vote_business
from business.goncourt_business import GoncourtBusiness
from business.novel_business import NovelBusiness
from business.round_business import RoundBusiness
from business.vote_business import VoteBusiness
from models.goncourt import Goncourt
from models.round import Round
from utils import input_utils


class UserView:

    @classmethod
    def display(cls):
        """
        Display the user interface and initialize the required business services.
        """
        goncourt_business = GoncourtBusiness()
        novel_business = NovelBusiness()
        round_business = RoundBusiness()
        vote_business = VoteBusiness()
        sessions: list[Goncourt] = goncourt_business.get_all()
        cls.select_session(novel_business, round_business, sessions, vote_business)

    @classmethod
    def select_session(cls, novel_business: NovelBusiness, round_business: RoundBusiness, sessions: list[Goncourt], vote_business: VoteBusiness):
        """
        Display all available Goncourt sessions and let the user select one.

        :param novel_business: Business service used to retrieve novels.
        :param round_business: Business service used to retrieve rounds.
        :param sessions: List of available Goncourt sessions.
        """
        print("========== CHOIX DE LA SESSION ==========\n")

        for index, session in enumerate(sessions, start=1):
            print(f"[{index}] Goncourt {session.year}")

        choice = input_utils.input_number("\nVeuillez choisir une session : ", 1, len(sessions))

        selected_year = sessions[choice - 1].year
        cls.select_round(novel_business, round_business, selected_year, vote_business)

    @classmethod
    def select_round(cls, novel_business: NovelBusiness, round_business: RoundBusiness, selected_year: int, vote_business: VoteBusiness):
        """
        Display all rounds available for a Goncourt session and let the user
        select one.

        :param novel_business: Business service used to retrieve novels.
        :param round_business: Business service used to retrieve rounds.
        :param selected_year: Year of the selected Goncourt session.
        """
        rounds = round_business.get_round_for_year(selected_year)
        loop_select_round = True
        while loop_select_round:
            print(f"\n========== PRIX GONCOURT {selected_year} ==========\n")
            print("0. Arreter")
            for index, round_ in enumerate(rounds, start=1):
                print(f"{index}. Afficher la sélection n°{round_.number} ({round_.date_round.strftime("%d/%m/%Y")})")
            print(f"{len(rounds)+1}. Afficher le résultat finale")
            if rounds:
                choice = input_utils.input_number("\nVotre choix : ", 0, len(rounds) + 1)
                if choice == 0:
                    loop_select_round = False
                    continue
                elif choice == len(rounds)+1:
                    cls.display_final_result_novels(vote_business, selected_year)
                else:
                    selected_round = rounds[choice - 1]
                    cls.display_round_novels(novel_business, selected_round)

    @classmethod
    def display_round_novels(cls, novel_business: NovelBusiness, selected_round: Round):
        """
        Display all novels belonging to the selected round.

        :param novel_business: Business service used to retrieve novels.
        :param selected_round: Round whose novels should be displayed.
        """
        print(f"\n========== SÉLECTION N°{selected_round.number} ==========\n")

        if selected_round.id_round:
            novels = novel_business.get_all_from_round(selected_round.id_round)

            for novel in novels:
                print(novel)

        input()

    @classmethod
    def display_final_result_novels(cls, vote_business: VoteBusiness, year:int):
        all_votes = vote_business.get_vote_for_year(year)
        all_votes.sort(key=lambda x: x.number_of_votes, reverse=True)
        for vote in all_votes:
            print(f"- {vote.novel.oneline_display()} ({vote.number_of_votes} votes)")
        input()
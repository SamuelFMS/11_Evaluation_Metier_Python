from typing import Optional
from xmlrpc.client import MAXINT

from business.goncourt_business import GoncourtBusiness
from business.novel_business import NovelBusiness
from business.round_business import RoundBusiness
from business.vote_business import VoteBusiness
from models.goncourt import Goncourt
from models.novel import Novel
from models.round import Round
from models.vote import Vote
from utils import input_utils


class PresidentView:
    @classmethod
    def display(cls):
        """
        Display the president interface and initialize the required business services.
        """
        goncourt_business = GoncourtBusiness()
        novel_business = NovelBusiness()
        round_business = RoundBusiness()
        vote_business = VoteBusiness()

        sessions: list[Goncourt] = goncourt_business.get_all()
        cls.select_session(novel_business, round_business, sessions, vote_business)

    @classmethod
    def select_session(cls, novel_business: NovelBusiness, round_business: RoundBusiness, sessions: list[Goncourt],
                       vote_business: VoteBusiness):
        """
        Display all available Goncourt sessions and let the user select one.

        :param novel_business: Business service used to manage novels.
        :param round_business: Business service used to retrieve rounds.
        :param sessions: List of available Goncourt sessions.
        """
        print("========== CHOIX DE LA SESSION ==========\n")

        for index, session in enumerate(sessions, start=1):
            print(f"[{index}] Goncourt {session.year}")

        choice = input_utils.input_number("\nVeuillez choisir une session : ", 1, len(sessions))

        selected_year = sessions[choice - 1].year
        cls.select_round(novel_business, round_business, vote_business, selected_year)

    @classmethod
    def select_round(cls, novel_business: NovelBusiness, round_business: RoundBusiness, vote_business: VoteBusiness,
                     selected_year: int):
        """
        Display all rounds of the selected Goncourt session and let the user
        choose a round to edit.

        :param novel_business: Business service used to manage novels.
        :param round_business: Business service used to retrieve rounds.
        :param selected_year: Year of the selected Goncourt session.
        """
        rounds = round_business.get_round_for_year(selected_year)

        display_select_round = True
        while display_select_round:
            print(f"\n========== PRIX GONCOURT {selected_year} ==========\n")
            print("0. Stop")
            for index, round_ in enumerate(rounds, start=1):
                assert round_.id_round
                print(f"{index}. Éditer la sélection n°{round_business.get_number(round_.id_round)}")
            print(f"{len(rounds) + 1}. Éditer les notes")
            if not rounds:
                return

            choice = input_utils.input_number("\nVotre choix : ", 0, len(rounds) + 1)

            if choice == 0:
                display_select_round = False
            elif choice == len(rounds) + 1:
                cls.edit_notes(vote_business, selected_year)
            else:
                selected_round = rounds[choice - 1]
                id_parent_round = selected_round.id_round_parent
                if id_parent_round is None:
                    previous_round = None
                else:
                    previous_round = round_business.get_round_by_id(id_parent_round)

                cls.display_round_novels(round_business, novel_business, selected_round, previous_round, selected_year)

    @classmethod
    def display_round_novels(cls,round_business:RoundBusiness, novel_business: NovelBusiness, selected_round: Round, previous_round: Optional[Round],
                             year: int):
        """
        Display the novels available for the selected round and allow the
        president to add or remove a novel.

        :param year:
        :param novel_business: Business service used to manage novels.
        :param selected_round: Round currently being edited.
        :param previous_round: Previous round used to determine available novels.
        """
        display_round = True
        while (display_round):
            assert selected_round.id_round
            print(f"\n========== SÉLECTION N°{round_business.get_number(selected_round.id_round)} ==========\n")

            if selected_round.id_round is None:
                return

            selected_novels = novel_business.get_all_from_round(selected_round.id_round)

            available_novels = cls.get_available_novels(novel_business, previous_round)

            cls.display_novels(available_novels, selected_novels)

            choice = input_utils.input_number("\nVotre choix : ", 0, len(available_novels))

            if choice == 0:
                display_round = False
                continue

            chosen_novel = available_novels[choice - 1]

            if chosen_novel.id_novel is None:
                return

            already_selected = any(novel.id_novel == chosen_novel.id_novel for novel in selected_novels)

            if already_selected:
                cls.remove_novel(novel_business, chosen_novel.id_novel, selected_round.id_round, year)
            else:
                cls.add_novel(novel_business, chosen_novel.id_novel, selected_round.id_round, year)

    @classmethod
    def get_available_novels(cls, novel_business: NovelBusiness, previous_round: Optional[Round]) -> list[Novel]:
        """
        Retrieve novels available for the selected round.

        :param novel_business: Business service used to retrieve novels.
        :param previous_round: Previous round of the Goncourt session.
        :return: List of novels available for selection.
        """
        if previous_round is None or previous_round.id_round is None:
            return novel_business.get_all()

        return novel_business.get_all_from_round(previous_round.id_round)

    @classmethod
    def display_novels(cls, available_novels: list[Novel], selected_novels: list[Novel]):
        """
        Display all available novels and mark already selected novels.

        :param available_novels: Novels available for selection.
        :param selected_novels: Novels already selected for the round.
        """
        print("[0] - Retour en arrière")

        selected_ids = {novel.id_novel for novel in selected_novels}

        for index, novel in enumerate(available_novels, start=1):
            marker = "✓" if novel.id_novel in selected_ids else " "
            print(f"[{index}] [{marker}] {novel.oneline_display()}")

    @classmethod
    def remove_novel(cls, novel_business: NovelBusiness, novel_id: int, round_id: int, year: int):
        """
        Remove a novel from the selected round.
        :param novel_business:
        :param novel_id:
        :param round_id:
        :param year:
        :return:
        """
        if novel_business.remove_novel_from_round(novel_id, round_id, year):
            print("Roman retiré avec succès.")
        else:
            print("Échec de la suppression du roman.")

    @classmethod
    def add_novel(cls, novel_business: NovelBusiness, novel_id: int, round_id: int, year: int):
        """
        Add a novel to the selected round.
        :param novel_business:
        :param novel_id:
        :param round_id:
        :param year:
        :return:
        """
        if novel_business.add_novel_to_round(novel_id, round_id, year):
            print("Roman ajouté avec succès.")
        else:
            print("Échec de l'ajout du roman.")

    @classmethod
    def edit_notes(cls, vote_business: VoteBusiness, year: int):
        """
        edit the notes available for the selected round.
        :param vote_business:
        :param year:
        :return:
        """
        changing_notes = True
        while changing_notes:
            list_vote: list[Vote] = vote_business.get_vote_for_year(year)

            print("[0] retour en arrière")
            index = 1
            for vote in list_vote:
                print(f"[{index}] {vote.novel.oneline_display()} ({vote.number_of_votes} votes)")
                index += 1
            choice = input_utils.input_number("\nVotre choix : ", 0, len(list_vote))
            if choice == 0:
                changing_notes = False
            else:
                vote = list_vote[choice - 1]
                new_note = input_utils.input_number("\nVotre note : ", 0, MAXINT)
                vote.number_of_votes = new_note
                vote_business.set_note(vote)

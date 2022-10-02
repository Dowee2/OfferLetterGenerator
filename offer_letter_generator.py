#!/usr/bin/env python3

"""
A Offer Letter Generator
"""
import datetime
import utils

__author__ = 'Anton Maynard'
__version__ = 'Fall 2022'
__pylint__ = '1.8.3.'


class OfferGenerator:
    """
    A class to generate offer letters
    """
    name = ""
    candidate_email = ""
    candidate_name = ""
    job_title = ""
    company_name = ""
    start_date = ""
    response_date = ""
    manager_name = ""
    manager_phone = ""
    dept_name = ""
    hr_person = ""

    def generateOfferLetter(self, offer_letter: str) -> str:
        """
        Generates an offer letter
        """
        print("Generating offer letter")
        today = datetime.date.today()
        offer_letter = offer_letter.replace("Template", "")
        offer_letter = offer_letter.replace("[todayâ€™s date]", str(today).strip())
        offer_letter = offer_letter.replace("[Candidate_name]", self.name.strip())
        offer_letter =offer_letter.replace("[Job_title]", self.job_title.strip())
        offer_letter = offer_letter.replace("[Company_name]", self.company_name.strip())
        offer_letter =offer_letter.replace("[Start Date]", self.start_date.strip())
        offer_letter = offer_letter.replace("[Manager_name]", self.manager_name.strip())
        offer_letter = offer_letter.replace("[date]", self.response_date.strip())
        offer_letter = offer_letter.replace("[HR person]", self.hr_person.strip())
        if utils.check_phone(self.manager_phone):
            offer_letter.replace("[mgr phone]", "manager_phone")
        else:
            print(f"Please enter a valid phone number for {self.manager_name}")
            input()
        offer_letter.replace("[HR person]", self.hr_person)

        return offer_letter


    def _check_for_empty_string(self, candidate: list):
            """
            Checks for empty strings in the candidate list and if there is one returns the index of the empty string
            """
            index = -1
            for item in candidate:
                if item.strip() == "":
                    return candidate.index(item)
            return index
        
    def parse_candidates_from_file(self, offer_letter_template, candidate_file: list):
        """
        Parses the candidate file and generates offer letters
        """
        
        self.company_name = candidate_file[1]
        if len(candidate_file) > 3:
            line_count = 5
            for candidate in candidate_file[4:len(candidate_file)]:
                candidate = candidate.split(",")
                while self._check_for_empty_string(candidate) != -1:
                    index_of_empty_string = self._check_for_empty_string(candidate)
                    position_header = candidate_file[3].split(",")
                    missing_info = input(f"Please enter a valid {position_header[index_of_empty_string]} on line {line_count} of the candidates list: ")
                    candidate[index_of_empty_string] = missing_info
                if len(candidate) > 8:
                    self.name = candidate[0]
                    self.candidate_email = candidate[1]
                    self.job_title = candidate[2]
                    self.dept_name = candidate[3]
                    self.start_date = candidate[4]
                    self.manager_name = candidate[5]
                    self.response_date = candidate[6]
                    self.manager_phone = candidate[7]
                    self.hr_person = candidate[8]
                    offer_letter = self.generateOfferLetter(offer_letter_template)
                    utils.generate_pdf(offer_letter, self.name)
                    line_count += 1
                else:
                    print(f"Please check the candidate list for {candidate} as it is missing some information")
                    input()
    
        else:
            print("Please provide a candidate list with atleast one candidate")
            input()
            
        
        
            
    

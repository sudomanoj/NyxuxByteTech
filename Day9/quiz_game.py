import json

class Player:
    score = 1
    @classmethod    
    def score_count(cls):
        next_score = cls.score
        cls.score += 1
        return next_score

    def player_name(self):
        name = self.name
        return name
    
question_file = 'newfile.json'        
class Quiz:
    def __init__(self, question_file):
        with open(question_file, 'r') as file:
            self.question_data = json.loads(file.read())

    def play_game(self, name):
        score = 0
        for question in self.question_data:
            question_format = f"""
            {question['question_no']}. {question['question']}
            a. {question['option']['a']}    b. {question['option']['b']}
            c. {question['option']['c']}    d. {question['option']['d']}
            """
            print(question_format)
            ans = input('Enter option a, b, c or d: ')
            if ans == question['answer']:
                score = Player.score_count()
        print(f'{name} scored : {score}')
        
 
name = input('Enter name of player: ')       
quiz_instance = Quiz(question_file)        
quiz_instance.play_game(name)

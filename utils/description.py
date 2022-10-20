from utils.get_docs_text import main

class Description:

    def __init__(self, template, doc_path):
        self.template = template
        self.doc_path = doc_path
        self.doc_text = None

    def read_text_file(self, filepath):
        
        with open(filepath) as f:
            lines = f.readlines()
            lines = [line for line in lines if line != '\n']
            return lines

    def get_doc_text(self, doc_id):
        #get text from google doc episode
        main(doc_id)

        with open(self.doc_path, 'r') as f:
            lines = f.readlines()
            self.doc_text = lines

    def make_sections(self):
        #loop thru topics, number them and indent timestamps or give them html for lists
        # new line means new topic
        # * means end of desc
        line, topic_number = 0, 1
        in_topic = False
        end_of_desc = '---' in self.doc_text[line]
        string = ''

        while not ('---' in self.doc_text[line] or '***' in self.doc_text[line]):
            if self.doc_text[line] == '\n':
                in_topic = False
                line += 1
                string += '\n'
                continue
            if in_topic:
                #add spaces or li
                string += '    {}'.format(self.doc_text[line]) 
                line += 1
                continue
            string += '{}. {}'.format(topic_number, self.doc_text[line])
            topic_number += 1
            in_topic = True
            line += 1

        return string + '\n'

    def make_description(self):
        #need desc, and to 
        lines = self.read_text_file(self.template)
        intro = lines[0]
        outro = lines[1:]

        body = self.make_sections()
        output = ''
        output += intro + '\n'
        output += body
        
        for line in outro[:-3]:
            output += line + '\n'

        for line in outro[-3:]:
            output += line

        return output


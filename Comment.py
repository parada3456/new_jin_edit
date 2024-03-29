from datetime import datetime, timedelta

class Comment:
    def __init__(self, chapter, user, context):
        self.__commentator = user
        self.__context = context
        self.__date_time = datetime.now()
        self.__chapter = chapter

    @property
    def commentator(self):
        return self.__commentator
    
    @property
    def context(self):
        return self.__context

    @property
    def date_time(self):
        return self.__date_time

    @property
    def date_time_str(self):
        return self.__date_time.strftime("%x %X")
    
    @property
    def chapter(self):
        return self.__chapter

    @property
    def report_list(self):
        return self.__report_list

    def update_time(self):
        self.__date_time = datetime.now()
        
    def show_comment(self):
        return {"user" : self.commentator.display_name,
                "chapter" : f"#{self.chapter.chapter_number} {self.chapter.name}",
                "context" : self.context,
                "date_time" : self.date_time_str,
                "context" : self.context}
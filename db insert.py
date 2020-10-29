def run():
    from polls.models import Question
    from django.utils import timezone

    def newQ(*args):
        for arg in args:
            q = Question(question_text=arg, pub_date=timezone.now())
            q.save()
        print(Question.objects.all())

    def newC(q: Question, *args):
        for arg in args:
            q.choice_set.create(choice_text=arg, votes=0)
        print(q.choice_set.all())

    newQ("What's up", "Coffee or tea", "2+2=?", "Have you ever own a pet", "Pineapple on pizza?",
         "Favourite gaming console")
    qo = Question.objects
    newC(qo.get(id=1), "Doing good", "Nothing much")
    newC(qo.get(id=2), "Coffee", "Tea")
    newC(qo.get(id=3), "3", "4", "5", "6")
    newC(qo.get(id=4), "Yes", "No")
    newC(qo.get(id=5), "Hell no", "Hell yes")
    newC(qo.get(id=6), "PC", "Play Station", "Xbox", "Mobile")

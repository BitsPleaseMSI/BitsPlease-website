from django.conf.urls import url
from .views import (
    QuestionListView,
    ProblemDetailView,
    ContestListView,
    ContestDetailView
)

urlpatterns = [
    url(r'^$', QuestionListView.as_view(), name="problems"),
    url(r'^problem/(?P<pk>\d+)', ProblemDetailView.as_view(), name="problem_detail"),
    url(r'^contest/$', ContestListView.as_view(), name="contests"),
    url(r'^contest/(?P<pk>\d+)', ContestDetailView.as_view(), name="contest_detail")

]

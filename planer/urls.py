from django.urls import path
from .views import (
    index,
    PositionListView,
    PositionCreateView,
    PositionDeleteView,
    TaskTypeListView,
    TaskTypeCreateView,
    TaskTypeDeleteView,
    WorkerListView,
    WorkerDetailView,
    WorkerCreateView,
    WorkerUpdateView,
    WorkerDeleteView,
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
)

urlpatterns = [
    path('', index, name='index'),
    path('positions/', PositionListView.as_view(), name='position-list'),
    path(
        'position/create/',
        PositionCreateView.as_view(),
        name='position-create'
    ),
    path(
        'position/<int:pk>/delete/',
        PositionDeleteView.as_view(),
        name='position-delete'
    ),

    path('tasktypes/', TaskTypeListView.as_view(), name='tasktype-list'),
    path(
        'tasktype/create/',
        TaskTypeCreateView.as_view(),
        name='tasktype-create'
    ),
    path(
        'tasktype/<int:pk>/delete/',
        TaskTypeDeleteView.as_view(),
        name='tasktype-delete'
    ),

    path('workers/', WorkerListView.as_view(), name='worker-list'),
    path(
        'worker/<int:pk>/',
        WorkerDetailView.as_view(),
        name='worker-detail'
    ),
    path(
        'worker/create/',
        WorkerCreateView.as_view(),
        name='worker-create'
    ),
    path(
        'worker/<int:pk>/update/',
        WorkerUpdateView.as_view(),
        name='worker-update'
    ),
    path(
        'worker/<int:pk>/delete/',
        WorkerDeleteView.as_view(),
        name='worker-delete'
    ),

    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task/create/', TaskCreateView.as_view(), name='task-create'),
    path(
        'task/<int:pk>/update/',
        TaskUpdateView.as_view(),
        name='task-update'
    ),
    path(
        'task/<int:pk>/delete/',
        TaskDeleteView.as_view(),
        name='task-delete'
    ),
]

app_name = 'planer'

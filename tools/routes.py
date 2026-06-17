from enum import Enum


class AppRoute(str, Enum):
    LOGIN = "./#/auth/login"
    REGISTRATION = "./#/auth/registration"
    DASHBOARD = "./#/dashboard"
    COURSES = "./#/courses"
    STUDENTS = "./#/students"
    CREATE_COURSES = "./#/courses/create"
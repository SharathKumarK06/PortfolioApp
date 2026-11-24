from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
@method_decorator(csrf_exempt, name="dispatch")
class AboutView(View):
    def get(self, request):
        data = {
            "id": 1,
            "full_name": "Adi Kesav",
            "title": "Python Developer",
            "bio": "A passionate developer building scalable applications.",
            "dob": "29/08/2002",
            "email": "adikesav@gmail.com",
            "contact": 9876543211,
            "location": "Kakkanad",
            "github_url": "https://github.com/adi-kesav",
            "linkedin_url": "https://linkedin.com/in/adi-kesav"
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt, name="dispatch")
class EducationView(View):
    def get(self, request):
        data = {
            "id": 101,
            "institution": "Luminar",
            "course": "Python Full Stack",
            "university": "ABC University",
            "location": "Cochin",
            "starting_year": "June 2026",
            "ending_year": "January 2027",
            "cgpa": "7.5",
            "description": "Completed Python Full Stack Development."
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt, name="dispatch")
class ProjectsView(View):
    def get(self, request):
        data = [
            {
                "id": 1,
                "title": "DietLense",
                "short_description": "AI-powered food recognition application.",
                "long_description": "An application that analyzes food images and provides nutritional information.",
                "technologies_used": [
                    "Python",
                    "Django",
                    "Google GenAI SDK"
                ],
                "live_url": "https://dietlense.example.com",
                "github_url": "https://github.com/username/dietlense",
                "image_url": "https://example.com/dietlense.jpg",
                "featured": True
            },
            {
                "id": 2,
                "title": "Interview Prep Blog",
                "short_description": "Educational application for programming interviews.",
                "long_description": "A platform for practicing technical interview questions and reading programming articles.",
                "technologies_used": [
                    "Python",
                    "Django",
                    "JavaScript"
                ],
                "live_url": "https://prep.example.com",
                "github_url": "https://github.com/username/interview-prep",
                "image_url": "https://example.com/interview.jpg",
                "featured": True
            }
        ]
        return JsonResponse(data, safe=False)

@method_decorator(csrf_exempt, name="dispatch")
class SkillsView(View):
    def get(self, request):
        data = [
            {
                "id": 1,
                "skill_name": "Python",
                "category": "Programming Language",
                "proficiency": "Advanced",
                "years_of_experience": 4
            },
            {
                "id": 2,
                "skill_name": "Django",
                "category": "Backend",
                "proficiency": "Advanced",
                "years_of_experience": 3
            },
            {
                "id": 3,
                "skill_name": "React",
                "category": "Frontend",
                "proficiency": "Intermediate",
                "years_of_experience": 2
            }
        ]
        return JsonResponse(data, safe=False)
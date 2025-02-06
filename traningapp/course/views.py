from django.shortcuts import render
from django.http import HttpResponse
from course.models import Courses

# View to add a course
def course(request):
    if request.method == 'POST':
        # Retrieve data from the POST request
        course_name = request.POST.get('course')
        duration = request.POST.get('due')
        fees = request.POST.get('fee')

        if course_name and duration and fees:
            # Save the course to the database
            obj = Courses()
            obj.course_name = course_name
            obj.duration = duration
            obj.fees = fees
            obj.save()
            return HttpResponse("Course added successfully.")
        else:
            return HttpResponse("All fields are required.", status=400)

    # Render the add course form
    return render(request, 'course/add courses.html')

# View to display all courses
def view(request):
    # Fetch all courses from the database
    courses = Courses.objects.all()
    context = {
        'a': courses  # Pass the courses to the templates
    }
    # Render the templates to display the courses
    return render(request, 'course/view course.html', context)

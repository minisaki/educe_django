from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def course_chat_room(request, course_id):
    try:
        # truy xuất khóa học với id đã cho được người dùng hiện tại tham gia
        course = request.user.courses_joined.get(id=course_id)
    except:
        # người dùng không phải là sinh viên của khóa học hoặc khóa học không tồn tại
        return HttpResponseForbidden()
    return render(request, 'chat/room.html', {'course': course})

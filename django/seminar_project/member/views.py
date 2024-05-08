import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import *



def create_member(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        id = data.get('id')
        email = data.get('email')
        is_leader = data.get('is_leader')
        hearts = data.get('hearts')

        member = Member(
            id = id,
            email = email,
            is_leader = is_leader,
            hearts = hearts
        )
        member.save()
        return JsonResponse({'message':'success'})
     
    return JsonResponse({'message':'POST 요청만 허용됩니다.'})

def read_member(request, pk):
    if request.method == 'GET':
        # get_object_or_404 함수를 사용하여 member 객체를 가져옵니다.
        # 객체가 존재하지 않는 경우, 404 에러를 반환합니다.
        member = get_object_or_404(Member, id=pk)
        
        # member 객체에서 필요한 정보를 추출하여 data 딕셔너리를 구성합니다.
        data = {
            'id': member.id,
            'email': member.email,
            'is_leader': member.is_leader,
            'hearts': member.hearts,
        }
        
        return JsonResponse(data, status=200)
    else:
        # GET 요청이 아닌 경우, 405 Method Not Allowed 에러를 반환합니다.
        return JsonResponse({'message': 'GET 요청만 허용됩니다.'}, status=405)
    
    
def update_member(request, pk):
    if request.method == 'PATCH':
        member = get_object_or_404(Member, id=pk)
        data = json.loads(request.body)
        
        # 요청된 데이터에서 회원 정보를 업데이트합니다.
        member.email = data.get('email', member.email)
        member.is_leader = data.get('is_leader', member.is_leader)
        member.hearts = data.get('hearts', member.hearts)
        
        member.save()  # 수정된 회원 정보를 데이터베이스에 저장합니다.
        
        # 수정 후의 회원 정보를 반환합니다.
        updated_data = {
            'id': member.id,
            'email': member.email,
            'is_leader': member.is_leader,
            'hearts': member.hearts
        }
        return JsonResponse(updated_data, status=200)
    else:
        # PATCH 요청이 아닌 경우, 405 Method Not Allowed 에러를 반환합니다.
        return JsonResponse({'message': 'PATCH 요청만 허용됩니다.'}, status=405)


def delete_member(request, pk):
    if request.method == 'DELETE':
        # get_object_or_404 함수를 사용하여 member 객체를 가져옵니다.
        # 객체가 존재하지 않는 경우, 404 에러를 반환합니다.
        member = get_object_or_404(Member, id=pk)
        member.delete()

        # 성공적으로 삭제했다는 메시지와 함께 삭제된 member의 id를 반환합니다.
        data = {
            "message": f"id: {pk} 회원 정보가 성공적으로 삭제되었습니다."
        }
        return JsonResponse(data, status=200)
    
    # DELETE 요청이 아닌 경우, 405 Method Not Allowed 에러를 반환합니다.
    return JsonResponse({'message': 'DELETE 요청만 허용됩니다.'}, status=405)


    

    

def add_heart(request, pk):
    member = Member.objects.get(id=pk)
    member.add_heart()
    return JsonResponse({'message': '하트가 추가되었습니다.'})

def manage_leader(request, pk):
    member = Member.objects.get(id=pk)
    
    # 이미 대표인 회원을 다시 대표로 임명하려는 경우
    if member.is_leader:
        return JsonResponse({'message': '이미 대표인 회원의 대표 자격을 박탈하세요.'}, status=400)
    
    # 동시에 최대 2명의 대표만 존재할 수 있음
    leaders_count = Member.objects.filter(is_leader=True).count()
    if leaders_count >= 2:
        return JsonResponse({'message': '대표는 2명 이상일 수 없습니다.'}, status=400)
    
    # 대표가 아닌 회원을 대표로 임명
    member.is_leader = True
    member.save()
    
    return JsonResponse({'message': f'{pk}(을)를 대표로 임명하였습니다.'})


def change_leader_status(request, pk):
    member = Member.objects.get(id=pk)
    member.toggle_leader()
    new_status = '임명되었습니다.' if member.is_leader else '박탈되었습니다.'
    return JsonResponse({'message': f'대표로 {new_status}'})

def get_all_members_info(request):
    members = Member.objects.all()
    members_info = list(members.values('id', 'email', 'is_leader', 'hearts'))
    return JsonResponse({
        'message': '모든 회원의 정보를 조회하기',
        'members': members_info,
        'member_count': len(members_info),
        'total_hearts': sum(member['hearts'] for member in members_info)
    })
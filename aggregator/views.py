from aggregator.models import expense_table
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import timedelta


def get_formatted_week(dt):
    '''
    Function that dates a date time object and returns formatted
    week information
    '''
    start = dt - timedelta(days=dt.weekday())
    end = start + timedelta(days=6)
    start_week = str(start.day) + start.strftime("%B") + str(start.year)
    end_week = str(end.day) + end.strftime("%B") + str(end.year)
    return start_week + '-' + end_week


class aggregator(APIView):
    def post(self, request, format=None):
        _category = request.data.get('category', False)
        _amount = request.data.get('amount', False)
        _date = request.data.get('date', False)

        if _category and _amount and _date:
            obj = expense_table(category=_category,
                                amount=float(_amount),
                                date=_date)
            obj.save()
            return Response(status=201, data={'Status': 'Insertion successful'})
        return Response(status=422, data={'Status': 'Error while processing data'})
    
    def get(self, request, format=None):
        objects = expense_table.objects.all()
        expense_data = {}

        for obj in objects:
            year, week, day = obj.date.isocalendar()
            week = get_formatted_week(obj.date)

            if obj.category not in expense_data:
                expense_data[obj.category] = {}
            if year not in expense_data[obj.category]:
                expense_data[obj.category][year] = {}
            if week not in expense_data[obj.category][year]:
                expense_data[obj.category][year][week] = 0
            expense_data[obj.category][year][week] += obj.amount        

        return Response(status=200, data=expense_data)
         

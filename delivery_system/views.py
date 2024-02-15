from rest_framework import generics, status
from rest_framework.response import Response
from .models import Pricing
from .serializers import PricingSerializer

class PricingDetail(generics.RetrieveAPIView):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer

    def retrieve(self, request, *args, **kwargs):
        # Get pricing instance
        instance = self.get_object()
       
        
        # Serialize pricing instance
        serializer = self.get_serializer(instance)
        data = serializer.data

        # Get total distance from request data
        total_distance = int(request.query_params.get('total_distance',0))
       
        #validate both Data Matching or Not

        #1.data from url
        U_zone=request.query_params.get('zone')
        U_organization_id=int(request.query_params.get('organization_id'))
        U_item_type=request.query_params.get('item_type')

        #2.data from database
        zone =data['zone']
        organization_id =instance.organization_id
        item_type =instance.item.type
       
        # #Matching the data
        # print("Data From Url:","zone:",U_zone ," organization_id:",U_organization_id," item_type:",U_item_type)
        # print("Data From Database:","zone:",zone ," organization_id:",organization_id," item_type:",item_type)
        
    
        
      
        # Calculate total price
      
        base_distance =int(data['base_distance_in_km']) 
        km_price = float(data['km_price'])
        fixed_price =float(data['fixed_price'])
        total_price = fixed_price
        if total_distance > base_distance:
            # if U_organization_id == organization_id:
            additional_distance = total_distance - base_distance
            total_price += additional_distance * km_price
        
            # Add total_price to response data
        data['total_price'] = round(total_price,2)
            
            
            # return Response( data["total_price"], status=status.HTTP_200_OK)
        return Response({"total_price": data["total_price"]}, status=status.HTTP_200_OK)





from django.shortcuts import render
import static
# Create your views here.
def home(request):
    emplist=[{
        'eid':12,
        'ename':'jyothi',
        'esal':40000
    },
    {
        'eid':13,
        'ename':'Neha',
        'esal':40000
    },
    {
        'eid':11,
        'ename':'Vijaya',
        'esal':40000
    },
    ]
    return render(request,'myapp/employes.html',{'emplist':emplist})
def getstudents(request):
    stulist=[
        {
            'stuid':12,
            'stuname':'raj',
            'stumarks':500
        },
        {
            'stuid':13,
            'stuname':'raj',
            'stumarks':500
        },
        {
            'stuid':14,
            'stuname':'raj',
            'stumarks':500
        },
    ]
    return render(request,'myapp/students.html',{'students':stulist})
def getproducts(request):
    productslist=[
        
  
    {
      "id": 1,
      "title": "Essence Mascara Lash Princess",
      "description": "The Essence Mascara Lash Princess is a popular .",
      "category": "beauty",
      "price": 9.99,
      
      
      
    },
    {
      "id": 2,
      "title": "Eyeshadow Palette with Mirror",
      "description": "The Eyeshadow Palette with Mirror offers a versatile.",
      "category": "beauty",
      "price": 19.99,
      
      
      
    },
    {
      "id": 3,
      "title": "Powder Canister",
      "description": "The Powder Canister is a finely milled setting powder designed to s.",
      "category": "beauty",
      "price": 14.99,
      
      
      
      
    },
    ]
    return render(request,'myapp/products.html',{'products':productslist})
def getcustomers(request):
     users=[
    {
      "id": 1,
      "Name": "Emily",
      "imgurl":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStDUOBUwJ49FyfucPIadoqNYXuQb0zWzXCHDd_zZbtYw&s=10",
      "age": 29,
      "gender": "female",
      
      "phone": "+81 965-431-3024",
    
          "country": "United States"
       
    },
    {
      "id": 2,
      "Name": "Michael",
      "imgurl":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSyLrVZhnluFtOs39QaCnl2F3QX6N44NEd8tfKBIbRufQ&s=10",
      "age": 36,
      "gender": "male",
      
      "phone": "+49 258-627-6644",
      
     
        "country": "United States"},
      
    {
      "id": 3,
      "Name": "Sophia",
      "imgurl":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuDKf_chzOU6QOxXi95xpi3yOiz4i1dzyAvoTFemQrPQ&s=10",
      "age": 43,
      "gender": "female",
      
      "phone": "+81 210-652-2785",
      
        "country": "United States"},
      
    ]
     return render(request,'myapp/customers.html',{'customers':users})
    
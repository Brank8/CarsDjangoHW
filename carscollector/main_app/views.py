from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car

# cars = [
#   {'name': 'Porsche', 'brand': 'Cayenne (2024)', 'description': 'The Cayenne is powered by a 3.0-liter turbocharged V6 producing 348 horsepower and 368 lb-ft of torque, giving it the ability to accelerate from zero to 60 MPH in 5.7 seconds (or 5.4 seconds with the optional Sport Chrono package). The Cayenne S is powered by a 4.0-liter twin-turbo V8 that boasts 468 horsepower and 442 lb-ft of torque. It can accelerate to 60 MPH from a standstill in just 4.6 seconds with the Sport Chrono package and continue on toward a top track speed of 169 MPH. A responsive eight-speed Tiptronic S transmission is included as standard equipment across the Cayenne line. Standard Porsche Active Suspension Management can automatically adapt to road surface conditions, strengthening both comfort and stability. An optional Sport Exhaust System provides a thrilling soundtrack as you rocket down the straightaway with your Porsche Cayenne.'},
#   {'name': 'Ferrari', 'brand': '488 Pista (2020)', 'description': 'The Ferrari 488 (Type F142M) is a mid-engine sports car produced by the Italian automobile manufacturer Ferrari. The car replaced the 458, being the first mid-engine Ferrari to use a turbocharged V8 since the F40. It was succeeded by the Ferrari F8. The car is powered by a 3.9-litre twin-turbocharged V8 engine, smaller in displacement but generating a higher power output than the 458`s naturally aspirated engine. The 488 GTB was named `The Supercar of the Year 2015` by car magazine Top Gear, as well as becoming Motor Trend`s 2017 `Best Driver`s Car`. Jeremy Clarkson announced the 488 Pista as his 2019 Supercar of the Year.'},
#   {'name': 'Ford', 'brand': 'Mustang (2024)', 'description': 'The new Mustang comes standard with an upgraded turbocharged 315-hp 2.3-liter four-cylinder EcoBoost engine with 350 pound-feet of torque. That`s 5 horsepower more than the previous Mustang, but still trails the last-gen EcoBoost Performance`s 330-hp. While every EcoBoost Mustang gets a 10-speed automatic transmission, the Mustang GT, which continues to offer a 5.0-liter V-8, has a six-speed manual standard. The last generation`s Coyote V-8 produced 450 horsepower with 420 pound-feet of torque, but the new unit is rated for 480 horsepower and 415 pound-feet of torque. The new Mustang steering feel and feedback are an area of obvious improvement. Ford says an optional performance exhaust increases output to 486 horsepower and 481 pound-feet. At our test track, a Mustang GT with the performance exhaust system ripped to 60 mph in 4.2 seconds; the EcoBoost wasn`t too far behind, hitting 60 mph in 4.5 seconds.'},
#   {'name': 'Lamborghini', 'brand': 'Urus (2023)', 'description': 'Born of pure Lamborghini DNA and oozing with beauty, performance, and speed, the 2023 Lamborghini Urus S is among the most accomplished super SUVs on the market today. The Urus embodies a visionary concept: An SUV with exotic exterior lines and the soul - and drive - of a great Italian sports car. That concept is even more refined in the form of the S, where performance, design, and exclusivity are further evolved to reveal even greater strength and a heightened perception of luxury. Expect maximum capability and comfort on any terrain and road condition you might encounter. After all, it`s a Lamborghini that can tow and carry a family, but with life-changing performance and plenty of sex appeal. Think of it as an exotic supercar that also functions as an SUV. Powered by a twin-turbo 4.0-liter V-8 engine that churns out 657 horsepower, the Urus S delivers heart-pumping performance and driving fun. You`ll get from zero to 60 mph in a mere 3.2 seconds and reach a searing top speed of 189 mph. The Urus S is lighter and more of a supercar than others in its class - and it more than lives up to its exotic status. Performance and pedigree. Beauty and speed. There is nothing else like it on the market.'},
# ]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})

def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'cars/detail.html', { 'car': car })

class CarCreate(CreateView):
    model = Car
    fields = '__all__'

class CarUpdate(UpdateView):
    model = Car
    fields = ['name', 'brand', 'description']

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars'
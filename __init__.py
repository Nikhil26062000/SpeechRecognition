#
# import speech_recognition as sr
# import webbrowser as web
#
#
# def main():
#     path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
#
#     r = sr.Recognizer()
#
#     with sr.Microphone() as source:
#         r.adjust_for_ambient_noise(source)
#
#         print("Please say something ")
#
#         audio = r.listen(source)
#
#         print("Reconizing Now ... ")
#
#         try:
#             dest = r.recognize_google(audio)
#             print("You have said : " + dest)
#
#             web.get(path).open(dest)
#
#         except Exception as e:
#             print("Error : " + str(e))
#
#
# if __name__ == "__main__":
#     main()


# import requests
# from pprint import pprint
# def weather_data(query):
# 	res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=****************************8&units=metric');
# 	return res.json();
# def print_weather(result,city):
# 	print("{}'s temperature: {}°C ".format(city,result['main']['temp']))
# 	print("Wind speed: {} m/s".format(result['wind']['speed']))
# 	print("Description: {}".format(result['weather'][0]['description']))
# 	print("Weather: {}".format(result['weather'][0]['main']))
# def main():
# 	city=input('Enter the city:')
# 	print()
# 	try:
# 	  query='q='+city;
# 	  w_data=weather_data(query);
# 	  print_weather(w_data, city)
# 	  print()
# 	except:
# 	  print('City name not found...')
# if __name__=='__main__':
# 	main()
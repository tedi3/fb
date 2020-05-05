from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver.chrome.options import Options 

# chromedriver = "/usr/bin/chromedriver"
# os.environ["webdriver.chrome.driver"] = chromedriver



class FbBot:
	def __init__(self,username,password):  
		self.username = username
		self.password = password
		
		#self.query = query
		#self.bot = webdriver.Chrome(chromedriver)

		chrome_options = Options()  
		chrome_options.add_argument("--headless")

		prefs = {"profile.default_content_setting_values.notifications" : 2}
		chrome_options.add_experimental_option("prefs",prefs)

		chrome_options.binary_location = os.getcwd()+"/bin/headless-chromium"   

		self.bot = webdriver.Chrome(executable_path=os.getcwd()+"/bin/chromedriver",chrome_options=chrome_options) 


		#self.bot = webdriver.Chrome(executable_path="/usr/bin/chromedriver")

		#  new metho on this class

	def login(self):
		bot = self.bot
		bot.get('https://facebook.com')
		time.sleep(4)
		email = bot.find_element_by_id('email')
		password = bot.find_element_by_id('pass')
		#email.clear()
		#password.clear()
		email.send_keys(self.username)
		password.send_keys(self.password)

		bot.find_element_by_id('loginbutton').click()

		time.sleep(18)

		#search = bot.find_element_by_class_name("_1frb")
		#search.send_keys(self.query)

	"""def like(self):
					bot = self.bot"""



	def search_person(self,name):


		url_person = 'https://www.facebook.com/alina.kashlinskaya'

		url = 'https://www.facebook.com/malitha.kck/about'

		url1 = 'https://www.facebook.com/malitha.kck/about_work_and_education'

		url2 = 'https://www.facebook.com/malitha.kck/about_places'

		url3 = 'https://www.facebook.com/malitha.kck/about_contact_and_basic_info'

		#contact_info,websites_and_links,basic_info -gender

		url4 = 'https://www.facebook.com/malitha.kck/about_family_and_relationships'

		#relationship,family_members


		url5 = 'https://www.facebook.com/malitha.kck/about_details'


		url6 = 'https://www.facebook.com/malitha.kck/about_life_events'



		#####

		friends = 'https://www.facebook.com/malitha.kck/friends'




		#/html[1]/body[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/a[1]/span[1]



		###
		photos = 'https://www.facebook.com/malitha.kck/photos'












		


		bot = self.bot

		bot.get('https://www.facebook.com/profile.php?id=100016988883380')

		#name =bot.find_element_by_class_name('j83agx80 bp9cbjyn')

		x = bot.find_element_by_xpath("/html[1]/body[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/h1[1]/div[1]")
		print(x)
        #title = utils.get_title(x, selectors)
        

		#print(name)



		#name = //div[@class='j83agx80 bp9cbjyn']
		#//div[@class='j83agx80 bp9cbjyn']

		#/html[1]/body[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/h1[1]/div[1]






	def group(self):
		bot = self.bot
		bot.get('group_link')
		time.sleep(18)
		#bot.find_element_by_class_name('_2yav').click()
		bot.find_element_by_css_selector("[title^='Files']").click()
		filelist = bot.find_element_by_class_name('_pu_')
		print(filelist)



fb = FbBot('saralinda@easy.com','$buddy032') # replace with login deatils

fb.login()
#fb.group()
fb.search_person("maltih")

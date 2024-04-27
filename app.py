import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image, AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.core.window import Window
from kivy.properties import ObjectProperty

import requests
import os

class container(GridLayout):
	
	response = ObjectProperty(None)
	urlInput = ObjectProperty(None)
	responsemain = ObjectProperty(None)
	filename = ObjectProperty(None)
	
	data_one = ObjectProperty(None)
	value_one = ObjectProperty(None)
	data_two = ObjectProperty(None)
	value_two = ObjectProperty(None)
	
	# eventListeners
	def request(self):
		try:
			if self.urlInput.text != "":
				self.req = requests.get(self.urlInput.text)
				self.response.text = str(self.req)
		except:
			self.response.text = "Erro"
	
	def requesttext(self):
		try:
			if self.urlInput.text != "":
				self.req = requests.get(self.urlInput.text)
				self.response.text = str(self.req)
				self.responsemain.text = self.req.text
		except:
			self.response.text = "baD::expression"
			self.responsemain.text = "baD::expression"
	
	def dir(self):
		try:
			if self.urlInput.text != "":
				self.req = requests.get(self.urlInput.text)
				self.response.text = str(self.req)
				self.responsemain.text = str(dir(self.req))
		except:
			self.response.text = "baD::expression"
			self.responsemain.text = "baD::expression"
	
	def help(self):
		try:
			if self.urlInput.text != "":
				self.req = requests.get(self.urlInput.text)
				self.response.text = str(self.req)
				self.responsemain.text = str(self.req.headers)
		except:
			self.response.text = "baD::expression"
			self.responsemain.text = "baD::expression"
	
	def json(self):
		try:
			if self.urlInput.text != "":
				if self.data_one.text != "":
					if self.value_one.text != "":
						if self.data_two.text != "":
							if self.value_two.text != "":
								self.payload = {self.data_one.text:self.value_one.text,self.data_two.text:self.value_two.text}
								self.req = requests.get(self.urlInput.text, params=self.payload)
								self.response.text = str(self.req)
								try:
									self.responsemain.text = str(self.req.json)
								except:
									self.responsemain.text = "linkError::No javascript Object Notation"
		
		except:
			self.response.text = "baD::expression"
			self.responsemain.text = "baD::expression"
			self.data_one.text = "baD::expression"
			self.value_one.text = "baD::expression"
			self.data_two.text = "baD::expression"
			self.value_two.text = "baD::expression"
	
	def payl(self):
		try:
			if self.urlInput.text != "":
				if self.data_one.text != "":
					if self.value_one.text != "":
						if self.data_two.text != "":
							if self.value_two.text != "":
								self.payload = {self.data_one.text:self.value_one.text,self.data_two.text:self.value_two.text}
								self.req = requests.get(self.urlInput.text, params=self.payload)
								self.response.text = str(self.req)
								try:
									self.responsemain.text = str(self.req.json())
								except:
									self.responsemain.text = "linkError::No javascript Object Notation"
		
		except:
			self.response.text = "baD::expression"
			self.responsemain.text = "baD::expression"
			self.data_one.text = "baD::expression"
			self.value_one.text = "baD::expression"
			self.data_two.text = "baD::expression"
			self.value_two.text = "baD::expression"
	
	def content(self):
		try:
			if self.urlInput.text != "":
				self.req = requests.get(self.urlInput.text)
				self.response.text = str(self.req)
				self.responsemain.text = str(self.req.content)
		except:
			self.response.text = "baD::expression"
			self.responsemain.text = "baD::expression"
	
	def clean(self):
		if self.urlInput.text != "" or not(self.urlInput.text != ""):
			if self.data_one.text != "" or not(self.data_one.text != ""):
				if self.data_one.text != "" or not(self.data_one.text != ""):
					if self.value_one.text != "" or not(self.value_one.text != ""):
						if self.value_two.text != "" or not(self.value_two.text != ""):
							
							self.response.text = ""
							self.responsemain.text = ""
							self.data_one.text = ""
							self.value_one.text = ""
							self.data_two.text = ""
							self.value_two.text = ""
	
	def postmethod(self):
		try:
			if self.urlInput.text != "":
				if self.data_one.text != "":
					if self.value_one.text != "":
						if self.data_two.text != "":
							if self.value_two.text != "":
								self.payload = {self.data_one.text:self.value_one.text,self.data_two.text:self.value_two.text}
								self.req = requests.post(self.urlInput.text, data=self.payload)
								self.response.text = str(self.req)
								try:
									self.responsemain.text = str(self.req.json()["form"])
								except:
									self.responsemain.text = "linkError::No javascript Object Notation"
		
		except:
			self.response.text = "baD::expression"
			self.responsemain.text = "baD::expression"
			self.data_one.text = "baD::expression"
			self.value_one.text = "baD::expression"
			self.data_two.text = "baD::expression"
			self.value_two.text = "baD::expression"
	
	def cook(self):
		try:
			if self.urlInput.text != "":
				self.req = requests.get(self.urlInput.text)
				self.response.text = str(self.req)
				self.responsemain.text = str(self.req.cookies)
		except:
			self.response.text = "baD::expression"
			self.responsemain.text = "baD::expression"
	
	def down(self):
		try:
			if self.urlInput.text != "":
				self.req = requests.get(self.urlInput.text)
				self.response.text = str(self.req)
				self.responsemain.text = str(self.req.content)
						
				with open("/storage/emulated/0/" + self.filetype.text,"wb") as f:
					f.write(self.req.content)
					
				
		except:
			self.response.text = "baD::expression"
			self.responsemain.text = "baD::Download"
	
			
class mainapp(App):
	def build(self):
		return container()
	
if __name__ == "__main__":
	mainapp().run()
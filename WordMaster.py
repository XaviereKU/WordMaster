import math
import sys
import random
import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import datetime
from functools import partial
import chardet

path = os.getcwd()
path2 = 'wordlist'
wordlistpath = os.path.join(path,path2)

root = Tk()

pbsets = []

def menus():
	menus = list(os.listdir(wordlistpath))
	return menus

def numberofproblems(args):
	file = os.path.join(wordlistpath,args)
	f = open(file,'r', encoding = 'utf-8')
	length = len(f.readlines())
	numbers = []
	i = 0
	while i < length:
		i = i +1
		numbers.append(i)
	selnofp.config(value = numbers)

def makeprobs(pbset, pbnum, pbtype):
	global pbsets
	pbnum = int(pbnum)
	file = os.path.join(wordlistpath,pbset)
	f = open(file, 'r', encoding = 'utf-8')
	lines = f.readlines()
	linelen = len(lines)+1
	choosen = random.sample(list(range(1,linelen)),pbnum)
	for i in choosen:
		pbsets.append(lines[i-1].strip().split())
	if '1' in pbtype:
		pblabel.configure(text = pbsets[0][0])
	else:
		pblabel.configure(text = pbsets[0][1])
	scorelabel.configure(text = '현재 점수 : {}/{}'.format(0,pbnum))
	return pbsets

def nextprob(pbsets, pbtype, answer):
	score = int(str(scorelabelhidden['text']))
	current = int(str(numberlabel['text']))
	if current < len(pbsets):
		if '1' in pbtype:
			if answer.strip() == pbsets[current][1]:
				print('정답')
				score = score + 1
				scorelabelhidden.configure(text = str(score))
				scorelabel.configure(text = '현재 점수 : {}/{}'.format(score,selnofp.get()))
		else:
			if answer.strip() == pbsets[current][0]:
				print('정답')
				score = score + 1
				scorelabelhidden.configure(text = str(score))
				scorelabel.configure(text = '현재 점수 : {}/{}'.format(score,selnofp.get()))

	current = current + 1
	if current >= len(pbsets):
		numberlabel.configure(text = str(current))
		scorelabel.configure(text = '최종 점수 : {}/{}'.format(score,selnofp.get()))
	else:
		if '1' in pbtype:
			numberlabel.configure(text = str(current))
			pblabel.configure(text = pbsets[current][0])
		else:
			numberlabel.configure(text = str(current))
			pblabel.configure(text = pbsets[current][1])


root.geometry('800x600')

clicked = StringVar()
clicked.set('문제 선택')
dummy = menus()
drop = OptionMenu(root, clicked, *dummy, command = numberofproblems)
drop.grid(column=1, row =1)

selnofp = ttk.Combobox(root, value = '')
selnofp.grid(column=2, row=1)

pbtype = StringVar()
pbtype.set('유형 선택')
prbtype = OptionMenu(root, pbtype, '1. 영단어보고 뜻 맞추기', '2. 뜻 보고 영단어 맞추기')
prbtype.grid(column=3, row=1)

pbmakebtn = Button(root, text = '문제 생성', command = lambda: pbsets == makeprobs(clicked.get(),selnofp.get(),pbtype.get()))
pbmakebtn.grid(column=4, row=1)

numberlabel = Label(root, text = '0')
scorelabelhidden = Label(root, text = '0')

pblabel = Label(root, text = '여기에 문제가 나옵니다.', width = 30)
pblabel.grid(column=1, row=2)

anstext = Text(root, width=30, height=2)
anstext.grid(column=2, row=2)

subbtn = Button(root, text = '제출', command = lambda: nextprob(pbsets, pbtype.get(), anstext.get("1.0","end")))
subbtn.grid(column=3, row=2)

scorelabel = Label(root, text='점수가 표기됩니다.', width = 30)
scorelabel.grid(column=4, row=4)


root.mainloop()
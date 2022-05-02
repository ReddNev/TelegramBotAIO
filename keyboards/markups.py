from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

btn_main = KeyboardButton('Главное меню')

""" Main Menu """
btn_info = KeyboardButton('Информация')
btn_purse = KeyboardButton('Кошелек')
main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_info, btn_purse)

""" Answers to Info Menu"""
btn_well = KeyboardButton('Курс валюты')
btn_test1 = KeyboardButton('Тестовая кнопка')
info_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_well, btn_test1, btn_main)

""" Answers to Purse Menu"""
btn_check = KeyboardButton('Остаток на счете')
btn_money = KeyboardButton('Потрачено денег')
purse_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_check, btn_money, btn_main)


# -*- coding: utf-8 -*-

import random

def home():
	if (session.correct_attempts == None):
		session.correct_attempts = 0
	if (session.number_of_attempts == None):
		session.number_of_attempts = 0
	session.random_number = random.randint(1,10)
	form = FORM(
		DIV(
			LABEL("Guess a Random Number from 1 to 10: "),
			INPUT(
				_type = "text",
				_name = "user_guess",
				),
			),
		INPUT(
			_type = "submit",
			_value = "Submit Guess",
			)
		)
	tally = A(
		"view tally",
		_href = URL(
			a = "guess",
			c = "c01",
			f = "tally",
			)
		)
	clear = A(
		"clear tally",
		_href = URL(
			a = "guess",
			c = "c01",
			f = "clear_tally",
			)
		)
	if (form.process().accepted):
		session.user_guess = form.vars.user_guess
		session.number_of_attempts = session.number_of_attempts + 1
		if (int(form.vars.user_guess) == session.random_number):
			session.correct_attempts = session.correct_attempts + 1
			redirect(
				URL(
					a = "guess",
					c = "c01",
					f = "correct_guess",
					)
				)
		else:
			redirect(
				URL(
					a = "guess",
					c = "c01",
					f = "wrong_guess",
					)
				)
	return dict(
		form = form,
		clear = clear,
		tally = tally,
		)
def correct_guess():
	home = A(
		"home",
		_href = URL(
			a = "guess",
			c = "c01",
			f = "home",
			)
		)
	tally = A(
		"view tally",
		_href = URL(
			a = "guess",
			c = "c01",
			f = "tally",
			)
		)
	clear = A(
		"clear tally",
		_href = URL(
			a = "guess",
			c = "c01",
			f = "clear_tally",
			)
		)
	return dict(
		home = home,
		clear = clear,
		tally = tally,
		)
def wrong_guess():
	home = A(
		"home",
		_href = URL(
			a = "guess",
			c = "c01",
			f = "home",
			)
		)
	tally = A(
		"view tally",
		_href = URL(
			a = "guess",
			c = "c01",
			f = "tally",
			)
		)
	clear = A(
		"clear tally",
		_href = URL(
			a = "guess",
			c = "c01",
			f = "clear_tally",
			)
		)
	return dict(
		home = home,
		clear = clear,
		tally = tally,
		)
def tally():
	if (
		(session.correct_attempts == None)
		or
		(session.number_of_attempts == None)
		):
		redirect(
			URL(
				a = "guess",
				c = "c01",
				f = "home",
				)
			)
	if (session.number_of_attempts == 0):
		session.percent_correct = 0
	else:
		session.percent_correct = (
			float(session.correct_attempts)
			/
			float(session.number_of_attempts)
			*
			100
			)
	home = A(
		"home",
		_href = URL(
			a = "guess",
			c = "c01",
			f = "home",
			)
		)
	tally = A(
		"view tally",
		_href = URL(
			a = "guess",
			c = "c01",
			f = "tally",
			)
		)
	clear = A(
		"clear tally",
		_href = URL(
			a = "guess",
			c = "c01",
			f = "clear_tally",
			)
		)
	return dict(
		home = home,
		clear = clear,
		tally = tally,
		)
def clear_tally():
	session.clear()
	redirect(
		URL(
			a = "guess",
			c = "c01",
			f = "home",
			)
		)
	return ()

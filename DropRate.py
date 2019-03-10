#OSRS DROP RATE
#python3
#dozhi
import random


def main ():
	print("OSRS Drop rate calc..")
	console()

def console():
	print("Drop chance calculator : 1 ")
	print("EXIT : 0")
	user_choice = input(">>")
	if int(user_choice) == 1:
		drop_chance_fun()
	elif int(user_choice) == 0:
		good_bye()
	else:
		print("Shit choice!")
		console()


def drop_chance_fun():
	drop_count = input("drop rate of item >>")
	kill_count = input("kill count >>")
	drop_rate_calc(kill_count , drop_count)
	drop_simulator_console(drop_count)

def drop_rate_calc(kill_count_value ,drop_count_value):
	print("Your drop chance are : " + drop_proc_calc(drop_count_value) + "%")
	kill_count_checker(kill_count_value , drop_count_value)


def drop_proc_calc(drop_count_value):
	return str(float(1/int(drop_count_value)))

def kill_count_checker(kill_count_value , drop_count_value):
	if int(kill_count_value) > 1:
		kill_drop_proc_cacl(int(kill_count_value) , int(drop_count_value))


def kill_drop_proc_cacl(kill_count_value , drop_count_value):
		item_drop_chance = 1- ((drop_count_value-1)/drop_count_value)**kill_count_value
		print("you chance of getting drop with this kc is : "+str(round(item_drop_chance*100))+"%")


def drop_simulator_console(kc_count):
	user_answer = input("Do you want to try drop simulator? 1/0 >>")
	if user_answer == "1":
		user_answer_2 = input("How much time to run it?")
		drop_simulator(kc_count , user_answer_2)
	elif user_answer == "0":
		good_bye()
	else:
		print(">>>>>>>>>>>>>>>>>>>>>>>>.")
		console()


def drop_simulator(kc_count , run_count):
	for _ in range(int(run_count)):
		sk = 0
		while True:
			sk+=1
			if random.randint(1 , int(kc_count)) == int(kc_count):
				break
		print("done at "+str(sk)+" kill count")


def good_bye():
	print("good bye")





if __name__ == "__main__":
    main()

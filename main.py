def get_sdnf_sknf(res_table, v_nums, variables):
	if len(res_table) != 2**v_nums:
		print(f"Вы ввели {len(res_table)} результатов, когда ожидалось {2**v_nums} результатов")
		input("Нажмите enter для завершения...")
	else:
		src_table = []

		for i in range(v_nums):
			src_table.append([])


		for i in range(v_nums):
			sign = 0
			multiplicity = 2 ** (v_nums - 1 - i)
			start_pos = 0

			for j in range(int((2 ** v_nums) / (2 ** (v_nums - 1 - i)))):
				for k in range(start_pos, start_pos + multiplicity):
					src_table[i].append(sign)

				sign = int(not bool(sign))
				start_pos += multiplicity


	d = {"sknf": "",
		 "sdnf": ""}

	signs = {"sknf1": "&", "sknf2": "v", "sdnf1": "v", "sdnf2": "&"}

	for i in range(len(src_table[0])):
		if res_table[i] == 0:
			sign = 0
			key = "sknf"
		elif res_table[i] == 1:
			sign = 1
			key = "sdnf"

		d[key] += "("
		for j in range(len(src_table)):
			if src_table[j][i] == sign:
				d[key] += variables[j]
			else:
				d[key] += f"¬{variables[j]}"

			if j != len(src_table) - 1:
				d[key] += f" {signs[key + '2']} "

		d[key] += f") {signs[key + '1']} "

	return d, src_table

def write_to_file(filename, d, src_table, res_table):
	with open(f"{filename}.txt", "w", encoding="utf-8") as file:
		file.write("")
		forwrite = f"Исходная таблица:\n{' '.join(variables)}  Результат таблицы истинности\n"
		file.writelines(forwrite)

		for i in range(len(src_table[0])):
			for j in range(len(src_table)):
				file.writelines(f"{src_table[j][i]} ")
			file.writelines(f"   {res_table[i]}\n")

		file.writelines("\n")
		file.writelines(f"СДНФ: {d['sdnf'][:-2]}\n")
		file.writelines(f"СКНФ: {d['sknf'][:-2]}")

	print(f"Результат записан в файл '{filename}.txt'")

if __name__ == "__main__":
	method = int(input("Вы хотите найти СДНФ и СКНФ по результирующему столбцу таблицы или по первому заданию дз ?\n\
Ввод (1 - столбец/2 - ДЗ): "))

	if method == 1:
		v_nums = int(input("Введите количество переменных: "))
		variables = []

		for i in range(v_nums):
			variables.append(input(f"Введите {i + 1} переменную (x, y, z и тд) : "))

		res_table = [int(i) for i in input(f"Введите через пробел {2**v_nums} результатов таблицы истинности\nВвод: ").split()]
		d, src_table = get_sdnf_sknf(res_table, v_nums, variables)
		write_to_file("result", d, src_table, res_table)

	elif method == 2:
		v_nums = 3
		variables = ["x", "y", "z"]

		N1 = int(input("Введите число N1: "))
		N2 = 256 - N1

		nums = [N1, N2]

		for i in range(len(nums)):
			res_table = [0 for i in range(2 ** v_nums)]
			binary = list(bin(nums[i]))[2:]

			for j in range(len(binary)):
				res_table[j] = int(binary[j])


			d, src_table = get_sdnf_sknf(res_table, v_nums, variables)
			write_to_file(f"N{i + 1}", d, src_table, res_table)

	input("Нажмите enter для завершения работы...")

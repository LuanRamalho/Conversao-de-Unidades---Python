import tkinter as tk
from tkinter import ttk, messagebox

# Função de conversão
def convert():
    measure_type = measure_type_var.get()
    unit_from = unit_from_var.get()
    unit_to = unit_to_var.get()
    try:
        value = float(value_entry.get())
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido.")
        return

    if not measure_type or not unit_from or not unit_to:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos corretamente.")
        return

    result = None

    if measure_type == 'massa':
        result = convert_mass(unit_from, unit_to, value)
    elif measure_type == 'volume':
        result = convert_volume(unit_from, unit_to, value)
    elif measure_type == 'combustível':
        result = convert_fuel(unit_from, unit_to, value)
    elif measure_type == 'velocidade':
        result = convert_speed(unit_from, unit_to, value)
    elif measure_type == 'dado':
        result = convert_data(unit_from, unit_to, value)
    elif measure_type == 'comprimento':
        result = convert_length(unit_from, unit_to, value)
    elif measure_type == 'temperatura':
        result = convert_temperature(unit_from, unit_to, value)
    elif measure_type == 'tempo':
        result = convert_time(unit_from, unit_to, value)

    result_label.config(text=f"{value} {unit_from} = {result} {unit_to}")

def populate_units(event):
    measure_type = measure_type_var.get()
    unit_from_combobox['values'] = units[measure_type]
    unit_to_combobox['values'] = units[measure_type]

# Conversões
units = {
    'massa': ["miligrama", "grama", "quilograma", "onça", "libra"],
    'volume': ["mililitro", "metro cúbico", "litro"],
    'combustível': ["litro", "galão"],
    'velocidade': ["kmh", "mph", "ms"],
    'dado': ["bit", "byte", "kilobyte", "megabyte", "gigabyte", "terabyte"],
    'comprimento': ["picômetro", "nanômetro", "micrômetro", "milímetro", "metro", "pé", "jarda", "polegada", "quilômetro"],
    'temperatura': ["Celsius", "Fahrenheit", "Kelvin"],
    'tempo': ["milissegundos", "segundos", "minutos", "horas", "dias", "semanas", "meses", "anos", "décadas", "séculos"]
}

# Funções de conversão
def convert_mass(from_unit, to_unit, value):
    conversions = {
        "miligrama": {"grama": 0.001, "quilograma": 1e-6, "onça": 3.5274e-5, "libra": 2.2046e-6},
        "grama": {"miligrama": 1000, "quilograma": 0.001, "onça": 0.035274, "libra": 0.00220462},
        "quilograma": {"miligrama": 1e6, "grama": 1000, "onça": 35.274, "libra": 2.20462},
        "onça": {"miligrama": 28349.5, "grama": 28.3495, "quilograma": 0.0283495, "libra": 0.0625},
        "libra": {"miligrama": 453592, "grama": 453.592, "quilograma": 0.453592, "onça": 16}
    }
    return value * (conversions[from_unit].get(to_unit, 1))

def convert_volume(from_unit, to_unit, value):
    conversions = {
        "mililitro": {"metro cúbico": 1e-6, "litro": 0.001},
        "metro cúbico": {"mililitro": 1e6, "litro": 1000},
        "litro": {"mililitro": 1000, "metro cúbico": 0.001}
    }
    return value * (conversions[from_unit].get(to_unit, 1))

def convert_fuel(from_unit, to_unit, value):
    conversions = {
        "litro": {"galão": 0.264172},
        "galão": {"litro": 3.78541}
    }
    return value * (conversions[from_unit].get(to_unit, 1))

def convert_speed(from_unit, to_unit, value):
    conversions = {
        "kmh": {"mph": 0.621371, "ms": 0.277778},
        "mph": {"kmh": 1.60934, "ms": 0.44704},
        "ms": {"kmh": 3.6, "mph": 2.23694}
    }
    return value * (conversions[from_unit].get(to_unit, 1))

def convert_data(from_unit, to_unit, value):
    conversions = {
        "bit": {"byte": 0.125, "kilobyte": 1.25e-4, "megabyte": 1.25e-7, "gigabyte": 1.25e-10, "terabyte": 1.25e-13},
        "byte": {"bit": 8, "kilobyte": 0.001, "megabyte": 1e-6, "gigabyte": 1e-9, "terabyte": 1e-12},
        "kilobyte": {"bit": 8000, "byte": 1000, "megabyte": 0.001, "gigabyte": 1e-6, "terabyte": 1e-9},
        "megabyte": {"bit": 8e6, "byte": 1e6, "kilobyte": 1000, "gigabyte": 0.001, "terabyte": 1e-6},
        "gigabyte": {"bit": 8e9, "byte": 1e9, "kilobyte": 1e6, "megabyte": 1000, "terabyte": 0.001},
        "terabyte": {"bit": 8e12, "byte": 1e12, "kilobyte": 1e9, "megabyte": 1e6, "gigabyte": 1000}
    }
    return value * (conversions[from_unit].get(to_unit, 1))

def convert_length(from_unit, to_unit, value):
    conversions = {
        "picômetro": {"nanômetro": 0.001, "micrômetro": 1e-6, "milímetro": 1e-9, "metro": 1e-12, "pé": 3.2808e-12, "jarda": 1.0936e-12, "polegada": 3.937e-11, "quilômetro": 1e-15},
        "nanômetro": {"picômetro": 1000, "micrômetro": 0.001, "milímetro": 1e-6, "metro": 1e-9, "pé": 3.2808e-9, "jarda": 1.0936e-9, "polegada": 3.937e-8, "quilômetro": 1e-12},
        "micrômetro": {"picômetro": 1e6, "nanômetro": 1000, "milímetro": 0.001, "metro": 1e-6, "pé": 3.2808e-6, "jarda": 1.0936e-6, "polegada": 3.937e-5, "quilômetro": 1e-9},
        "milímetro": {"picômetro": 1e9, "nanômetro": 1e6, "micrômetro": 1000, "metro": 0.001, "pé": 0.00328084, "jarda": 0.00109361, "polegada": 0.0393701, "quilômetro": 1e-6},
        "metro": {"picômetro": 1e12, "nanômetro": 1e9, "micrômetro": 1e6, "milímetro": 1000, "pé": 3.28084, "jarda": 1.09361, "polegada": 39.3701, "quilômetro": 0.001},
        "pé": {"picômetro": 3.048e11, "nanômetro": 3.048e8, "micrômetro": 3.048e6, "milímetro": 304.8, "metro": 0.3048, "jarda": 0.333333, "polegada": 12, "quilômetro": 0.0003048},
        "jarda": {"picômetro": 9.144e11, "nanômetro": 9.144e8, "micrômetro": 9.144e6, "milímetro": 914.4, "metro": 0.9144, "pé": 3, "polegada": 36, "quilômetro": 0.0009144},
        "polegada": {"picômetro": 2.54e10, "nanômetro": 2.54e7, "micrômetro": 2.54e4, "milímetro": 25.4, "metro": 0.0254, "pé": 0.0833333, "jarda": 0.0277778, "quilômetro": 2.54e-5},
        "quilômetro": {"picômetro": 1e15, "nanômetro": 1e12, "micrômetro": 1e9, "milímetro": 1e6, "metro": 1000, "pé": 3280.84, "jarda": 1094, "polegada": 39370.1}
    }
    return value * (conversions[from_unit].get(to_unit, 1))

def convert_temperature(from_unit, to_unit, value):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return (value * 9/5) + 32 if to_unit == "Fahrenheit" else value + 273.15
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    else:  # Kelvin
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32

def convert_time(from_unit, to_unit, value):
    conversions = {
        "milissegundos": {"segundos": 1e-3, "minutos": 1.66667e-5, "horas": 2.77778e-7, "dias": 1.15741e-8, "semanas": 1.65344e-9, "meses": 3.80517e-10, "anos": 3.16887e-11, "décadas": 3.16887e-12, "séculos": 3.16887e-13},
        "segundos": {"milissegundos": 1000, "minutos": 1/60, "horas": 1/3600, "dias": 1/86400, "semanas": 1/604800, "meses": 1/2629743, "anos": 1/31557600, "décadas": 1/315576000, "séculos": 1/3155760000},
        "minutos": {"milissegundos": 60000, "segundos": 60, "horas": 1/60, "dias": 1/1440, "semanas": 1/10080, "meses": 1/43800, "anos": 1/525600, "décadas": 1/5256000, "séculos": 1/52560000},
        "horas": {"milissegundos": 3600000, "segundos": 3600, "minutos": 60, "dias": 1/24, "semanas": 1/168, "meses": 1/730, "anos": 1/8760, "décadas": 1/87600, "séculos": 1/876000},
        "dias": {"milissegundos": 86400000, "segundos": 86400, "minutos": 1440, "horas": 24, "semanas": 1/7, "meses": 1/30.4375, "anos": 1/365.25, "décadas": 1/3652.5, "séculos": 1/36525},
        "semanas": {"milissegundos": 604800000, "segundos": 604800, "minutos": 10080, "horas": 168, "dias": 7, "meses": 1/4.34524, "anos": 1/52.1429, "décadas": 1/521.429, "séculos": 1/5214.29},
        "meses": {"milissegundos": 2629746000, "segundos": 2629743, "minutos": 43800, "horas": 730, "dias": 30.4375, "semanas": 4.34524, "anos": 1/12, "décadas": 1/120, "séculos": 1/1200},
        "anos": {"milissegundos": 31557600000, "segundos": 31557600, "minutos": 525600, "horas": 8760, "dias": 365.25, "semanas": 52.1429, "meses": 12, "décadas": 10, "séculos": 0.01},
        "décadas": {"milissegundos": 315576000000, "segundos": 315576000, "minutos": 5256000, "horas": 87600, "dias": 3652.5, "semanas": 521.429, "meses": 120, "anos": 10, "séculos": 0.1},
        "séculos": {"milissegundos": 3155760000000, "segundos": 3155760000, "minutos": 52560000, "horas": 876000, "dias": 36525, "semanas": 5214.29, "meses": 1200, "anos": 100, "décadas": 10},
    }
    return value * (conversions[from_unit].get(to_unit, 1))

# Criando a janela principal
root = tk.Tk()
root.title("Conversor de Unidades")
root.configure(bg="cyan")  # Fundo claro e suave
root.geometry("400x350")  # Tamanho da janela

# Variáveis
measure_type_var = tk.StringVar()
unit_from_var = tk.StringVar()
unit_to_var = tk.StringVar()

# Estilo para widgets
style = ttk.Style()
style.configure("TFrame", background="cyan")  # Cor do fundo do frame
style.configure("TLabel", background="cyan", font=("Helvetica", 12), foreground="#333333")  # Fonte e cor dos labels
style.configure("TCombobox", font=("Helvetica", 12), width=20)  # Estilo da combobox
style.configure("TEntry", font=("Helvetica", 12), width=18)  # Estilo da entry

# Layout
frame = ttk.Frame(root, padding="20", relief="solid", borderwidth=2)
frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

# Tipo de medida
ttk.Label(frame, text="Tipo de Medida:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
measure_type_combobox = ttk.Combobox(frame, textvariable=measure_type_var, values=list(units.keys()))
measure_type_combobox.grid(row=0, column=1, padx=10, pady=5)
measure_type_combobox.bind("<<ComboboxSelected>>", populate_units)

# Unidade de origem
ttk.Label(frame, text="Unidade de Origem:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
unit_from_combobox = ttk.Combobox(frame, textvariable=unit_from_var)
unit_from_combobox.grid(row=1, column=1, padx=10, pady=5)

# Unidade de destino
ttk.Label(frame, text="Unidade de Destino:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
unit_to_combobox = ttk.Combobox(frame, textvariable=unit_to_var)
unit_to_combobox.grid(row=2, column=1, padx=10, pady=5)

# Valor
ttk.Label(frame, text="Valor:").grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
value_entry = ttk.Entry(frame)
value_entry.grid(row=3, column=1, padx=10, pady=5)

# Botão de conversão
convert_button = tk.Button(frame, text="Converter", command=convert , font=("Arial", 12, "bold") , bg="#006400" , fg="#FFFFE0")
convert_button.grid(row=4, columnspan=2, pady=10)

# Resultado
result_label = ttk.Label(frame, text="", font=("Helvetica", 12, "bold"), foreground="#4CAF50")
result_label.grid(row=5, columnspan=2, pady=10)

# Tornando a interface mais colorida e com melhores espaçamentos
root.mainloop()


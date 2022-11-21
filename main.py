#!/usr/bin/env python3

london_co = { "r1": {"location": "21 New Globe Walk",
                                "vendor": "Cisco",
                                        "model": "4451",
                                                "ios": "15.4",
                                                        "ip": "10.255.0.1"
                                                            },
                "r2": {
                            "location": "21 New Globe Walk",
                                    "vendor": "Cisco",
                                            "model": "4451",
                                                    "ios": "15.4",
                                                            "ip": "10.255.0.2"
                                                                },
                    "sw1": {
                                "location": "21 New Globe Walk",
                                        "vendor": "Cisco",
                                                "model": "3850",
                                                        "ios": "3.6.XE",
                                                                "ip": "10.255.0.101",
                                                                        "vlans": "10,20,30",
                                                                                "routing": True
                                                                                    }
                    }

a = list(london_co['r1'].keys())
user_input = input("Введите имя устройства: ")
user_input_2 = input(f"Введите имя параметра {a}: ")
if user_input in list(london_co.keys()) and user_input_2 in a:
    print(london_co[user_input][user_input_2.lower()])
else:
    print('Такого параметра нет')

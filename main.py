class Carbase:
    def __init__(self, car_type, brand, photo_le_name, carrying):
        self.car_type = car_type
        self.photo_le_name = photo_le_name
        self.brand = brand
        self.carrying = carrying

    def get_photo_le_ext(self):
        tp = self.photo_le_name[self.photo_le_name.find('.') + 1:]
        return tp


class Car(Carbase):
    def __init__(self, car_type, brand, photo_le_name, carrying, passenger_seats_count):
        super().__init__(car_type, brand, photo_le_name, carrying)
        self.passenger_seats_count = passenger_seats_count


class Truck(Carbase):
    def __init__(self, car_type, brand, photo_le_name, carrying, body_whl):
        super().__init__(car_type, brand, photo_le_name, carrying)
        self.body_whl = body_whl
        params = self.body_whl.split('x')
        self.body_width = params[0]
        self.body_height = params[1]
        self.body_length = params[2]

    def get_body_volume(self):
        fa = float(self.body_width) * float(self.body_height) * float(self.body_length)
        return fa


class Specmachine(Carbase):
    def __init__(self, car_type, brand, photo_le_name, carrying, extra):
        super().__init__(car_type, brand, photo_le_name, carrying)
        self.extra = extra

    def __str__(self):
        super().__str__()

    def __repr__(self):
        return self.extra


def get_car_list(filename):
    car_list = []
    with open(filename, 'r') as input_file:
        data = input_file.readlines()
        for obj in data:
            obj_info = obj.split(';')
            if obj_info[0] == 'car' or obj_info[0] == 'truck' or obj_info[0] == 'spec_machine':
                car_type = obj_info[0]
                brand = obj_info[1]
                photo_le_name = obj_info[3]
                carrying = obj_info[5]

                if obj_info[0] == 'car':
                    passenger_seats_count = obj_info[2]
                    machine = Car(car_type, brand, photo_le_name, carrying, passenger_seats_count)
                    car_list.append(machine)
                elif obj_info[0] == 'truck':
                    body_whl = obj_info[4]
                    if len(body_whl) == 0:
                        body_whl = '0x0x0'
                    machine = Truck(car_type, brand, photo_le_name, carrying, body_whl)
                    car_list.append(machine)
                elif obj_info[0] == 'spec_machine':
                    extra = obj_info[6]
                    machine = Specmachine(car_type, brand, photo_le_name, carrying, extra)
                    car_list.append(machine)
            else:
                continue

    return car_list


def main():
    pass


if __name__ == '__main__':
    main()

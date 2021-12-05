import pandas as pd

VALUES = [i for i in range(6)]
ZERO = [0]
ONE = [1]
GENDER_VAL = ['Female', 'Male']
SATISFACTION_VAL = ['neutral or dissatisfied', 'satisfied']
TRAVEL_VAL = ['Business travel', 'Personal Travel']
CLASS_VAL = ['Business', 'Eco', 'Eco Plus']


COLUMNS = ['Age', 'Flight Distance', 'Departure Delay in Minutes',
           'Arrival Delay in Minutes', 'Gender_Female', 'Gender_Male',
           'satisfaction_neutral or dissatisfied', 'satisfaction_satisfied',
           'Type of Travel_Business travel', 'Type of Travel_Personal Travel',
           'Class_Business', 'Class_Eco', 'Class_Eco Plus',
           'Inflight wifi service_0', 'Inflight wifi service_1',
           'Inflight wifi service_2', 'Inflight wifi service_3',
           'Inflight wifi service_4', 'Inflight wifi service_5',
           'Departure/Arrival time convenient_0',
           'Departure/Arrival time convenient_1',
           'Departure/Arrival time convenient_2',
           'Departure/Arrival time convenient_3',
           'Departure/Arrival time convenient_4',
           'Departure/Arrival time convenient_5', 'Ease of Online booking_0',
           'Ease of Online booking_1', 'Ease of Online booking_2',
           'Ease of Online booking_3', 'Ease of Online booking_4',
           'Ease of Online booking_5', 'Gate location_0', 'Gate location_1',
           'Gate location_2', 'Gate location_3', 'Gate location_4',
           'Gate location_5', 'Food and drink_0', 'Food and drink_1',
           'Food and drink_2', 'Food and drink_3', 'Food and drink_4',
           'Food and drink_5', 'Online boarding_0', 'Online boarding_1',
           'Online boarding_2', 'Online boarding_3', 'Online boarding_4',
           'Online boarding_5', 'Seat comfort_0', 'Seat comfort_1',
           'Seat comfort_2', 'Seat comfort_3', 'Seat comfort_4', 'Seat comfort_5',
           'Inflight entertainment_0', 'Inflight entertainment_1',
           'Inflight entertainment_2', 'Inflight entertainment_3',
           'Inflight entertainment_4', 'Inflight entertainment_5',
           'On-board service_0', 'On-board service_1', 'On-board service_2',
           'On-board service_3', 'On-board service_4', 'On-board service_5',
           'Leg room service_0', 'Leg room service_1', 'Leg room service_2',
           'Leg room service_3', 'Leg room service_4', 'Leg room service_5',
           'Baggage handling_1', 'Baggage handling_2', 'Baggage handling_3',
           'Baggage handling_4', 'Baggage handling_5', 'Checkin service_0',
           'Checkin service_1', 'Checkin service_2', 'Checkin service_3',
           'Checkin service_4', 'Checkin service_5', 'Inflight service_0',
           'Inflight service_1', 'Inflight service_2', 'Inflight service_3',
           'Inflight service_4', 'Inflight service_5', 'Cleanliness_0',
           'Cleanliness_1', 'Cleanliness_2', 'Cleanliness_3', 'Cleanliness_4',
           'Cleanliness_5']

col = ['Age', 'Flight Distance']


def assert_numeric(input: dict, output: dict, key: str, col: str):
    if key not in input.keys():
        output[col] = ZERO
    else:
        output[col] = [input[key]]


def assert_categorical_str(input: dict, output: dict, key: str, col: str, val_enums: list[str]):
    check = [i for i in range(len(val_enums))]
    val_cols = []
    for val in val_enums:
        real_col = f"{col}_{val}"
        val_cols.append(real_col)

    exist = key in input.keys()
    if exist:
        val = input[key]
        if val in check:
            for i in range(len(val_cols)):
                if val == i:
                    output[val_cols[i]] = ONE
                else:
                    output[val_cols[i]] = ZERO
        else:
            for i in range(len(val_cols)):
                output[val_cols[i]] = ZERO

    else:
        for i in range(len(val_cols)):
            output[val_cols[i]] = ZERO


def assert_categorical_num(input: dict, output: dict, key: str, col: str):
    val_cols = []
    for VAL in VALUES:
        real_col = f"{col}_{str(VAL)}"
        val_cols.append(real_col)

    exist = key in input.keys()
    if exist:
        val = input[key]
        if val in VALUES:
            for VAL in VALUES:
                if val == VAL:
                    output[val_cols[VAL]] = ONE
                else:
                    output[val_cols[VAL]] = ZERO
        else:
            for VAL in VALUES:
                output[val_cols[VAL]] = ZERO

    else:
        for VAL in VALUES:
            output[val_cols[VAL]] = ZERO


def sanitize(input: dict) -> dict:
    out = {}

    assert_numeric(input, out, 'age', 'Age')
    assert_numeric(input, out, 'flight_distance', 'Flight Distance')
    assert_numeric(input, out, 'delay', 'Departure Delay in Minutes')
    assert_numeric(input, out, 'arrival', 'Arrival Delay in Minutes')

    assert_categorical_str(input, out, 'gender', 'Gender', GENDER_VAL)
    assert_categorical_str(input, out, 'satisfied',
                           'satisfaction', SATISFACTION_VAL)
    assert_categorical_str(input, out, 'travel_type',
                           'Type of Travel', TRAVEL_VAL)
    assert_categorical_str(input, out, 'class', 'Class', CLASS_VAL)

    assert_categorical_num(input, out, 'wifi', 'Inflight wifi service')
    assert_categorical_num(
        input, out, 'departure_arrival_convenient', 'Departure/Arrival time convenient')
    assert_categorical_num(input, out, 'online_booking',
                           'Ease of Online booking')
    assert_categorical_num(input, out, 'gate_location', 'Gate location')
    assert_categorical_num(input, out, 'food_drink', 'Food and drink')
    assert_categorical_num(input, out, 'online_boarding', 'Online boarding')
    assert_categorical_num(input, out, 'seat_comfort', 'Seat comfort')
    assert_categorical_num(input, out, 'entertainment',
                           'Inflight entertainment')
    assert_categorical_num(input, out, 'onboard_service', 'On-board service')
    assert_categorical_num(input, out, 'leg_room_service', 'Leg room service')
    assert_categorical_num(input, out, 'baggage', 'Baggage handling')
    out.pop('Baggage handling_0')
    assert_categorical_num(input, out, 'checkin', 'Checkin service')
    assert_categorical_num(input, out, 'inflight', 'Inflight service')
    assert_categorical_num(input, out, 'cleanliness', 'Cleanliness')

    # print(out)
    return out


def to_dataframe(input) -> pd.DataFrame:
    df = pd.DataFrame.from_dict(sanitize(input))
    df[COLUMNS]

    return df

class CarPark:
    def __init__(self):
        self.daily_total = 0

    def calculate_price(self, day, arrival_hour, parking_hours, frequent_parking_number):
        fpn = [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999]
        if not (1 <= day <= 7) or not (0 <= arrival_hour <= 23) or not (0 < parking_hours <= 24):
            print("Invalid input. Please enter valid values.")
            return
        if 0 <= arrival_hour < 8:
            print("Parking is not allowed between Midnight and 08:00.")
            return

        base_price = 0

        if day == "Sunday" and arrival_hour < 16 and parking_hours <= 8:
            base_price = parking_hours * 2
        elif day == "Sunday" and 16 <= arrival_hour <= 23 and parking_hours <= 6:
            base_price = parking_hours * 2

        elif day == "Monday" and arrival_hour < 16 and parking_hours <= 2:
            base_price = parking_hours * 10
        elif day == "Monday" and 16 <= arrival_hour <= 23 and parking_hours <= 6:
            base_price = parking_hours * 2

        elif day == "Tuesday" and arrival_hour < 16 and parking_hours <= 2:
            base_price = parking_hours * 10
        elif day == "Tuesday" and 16 <= arrival_hour <= 23 and parking_hours <= 6:
            base_price = parking_hours * 2

        elif day == "Wednesday" and arrival_hour < 16 and parking_hours <= 2:
            base_price = parking_hours * 10
        elif day == "Wednesday" and 16 <= arrival_hour <= 23 and parking_hours <= 6:
            base_price = parking_hours * 2

        elif day == "Thursday" and arrival_hour < 16 and parking_hours <= 2:
            base_price = parking_hours * 10
        elif day == "Thursday" and 16 <= arrival_hour <= 23 and parking_hours <= 6:
            base_price = parking_hours * 2

        elif day == "Friday" and arrival_hour < 16 and parking_hours <= 2:
            base_price = parking_hours * 10
        elif day == "Friday" and 16 <= arrival_hour <= 23 and parking_hours <= 6:
            base_price = parking_hours * 2

        elif day == "Saturday" and arrival_hour < 16 and parking_hours <= 4:
            base_price = parking_hours * 10
        elif day == "Saturday" and 16 <= arrival_hour <= 23 and parking_hours <= 6:
            base_price = parking_hours * 2

        # Check frequent parking number and calculate discount
        discounted_price = base_price
        if frequent_parking_number in fpn and arrival_hour < 16:
            discounted_price = base_price* 0.5
        elif frequent_parking_number in fpn and 23 < arrival_hour > 16:
            discounted_price = base_price* 0.9
        else:
            print("Invalid frequent parking number. No discount applied.")

        # Display the calculated price
        print(f"Price to park: ${discounted_price:.2f}")

        # Add payment to the daily total
        self.daily_total += discounted_price

    def end_of_day_summary(self):
        print(f"\nDaily Total: ${self.daily_total:.2f}")

def main():
    car_park = CarPark()

    # Task 1
    day = int(input("Enter the day (1-7, where 1 is Monday and 7 is Sunday): "))
    arrival_hour = int(input("Enter the hour of arrival (0-23): "))
    parking_hours = int(input("Enter the number of hours to leave the car: "))
    frequent_parking_number = int(input("Enter the frequent parking number (if available): "))

    car_park.calculate_price(day, arrival_hour, parking_hours, frequent_parking_number)

    # Task 2
    payment_amount = float(input("Enter the amount paid: "))
    if payment_amount < car_park.daily_total:
        print("Insufficient payment. Please pay the full amount.")
    else:
        car_park.daily_total += payment_amount  # Update daily_total by subtracting the payment
        print("Payment received. Thank you!")
    # Task 3
    car_park.end_of_day_summary()

if __name__ == "__main__":
    main()

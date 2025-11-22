from gpiozero import LED
import time
from enum import Enum

class PaymentStatus(Enum):
  PENDING = 'pending'
  APPROVED = 'approved'
  DECLINED = 'declined'

class PaymentStatusIndicator:
  """Simulates payment status LED feedback"""

  def __init__(self, pin=17):
    self.led = LED(pin)

  def show_status(self, status: PaymentStatus):
    """Display payment status via LED pattern"""
    print(f"\nPayment Status: {status.value}")

    if status == PaymentStatus.PENDING:
      # Slow pulse
      print(' LED: Slow pulsing (pending)...')
      for _ in range(3):
        self.led.on()
        time.sleep(0.8)
        self.led.off()
        time.sleep(0.8)

    elif status == PaymentStatus.APPROVED:
      # Quick triple blink
      print(" LED: Quick triple blink (approved)")
      for _ in range(3):
        self.led.on()
        time.sleep(0.1)
        self.led.off()
        time.sleep(0.1)

    elif status == PaymentStatus.DECLINED:
      # Long solid on
      print(" LED: Solid on for 2 seconds (declined)")
      self.led.on()
      time.sleep(2)
      self.led.off()

  def cleanup(self):
    self.led.close()

# Demo
if __name__ == '__main__':
  indicator = PaymentStatusIndicator()

  # Simulate payment flow
  print('Simulating payment terminal...')

  indicator.show_status(PaymentStatus.PENDING)
  time.sleep(1)

  indicator.show_status(PaymentStatus.APPROVED)
  time.sleep(1)

  indicator.show_status(PaymentStatus.DECLINED)

  indicator.cleanup()
  print('\nDemo complete.')
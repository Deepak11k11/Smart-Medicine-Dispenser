import cv2
import serial
import serial.tools.list_ports
import continuous_threading

BAUD_RATE = 9600
TIMEOUT = 1

ser = serial.Serial()
ser.baudrate = BAUD_RATE
ser.timeout = TIMEOUT

def connect_to_port():
    port = None
    ports = []
    try:
        ports = [f"COM{i+1}" for i in range(256)]
    except Exception as e:
        print(e)
    
    for port in ports:
        try:
            ser.port = port
            ser.open()
            break
        except Exception as e:
            pass
    else:
        print("Not Connected")
        return

connect_to_port()

cap = cv2.VideoCapture(0)
qr_code_detector = cv2.QRCodeDetector()

while True:
    ret, frame = cap.read()    
    retval, decoded_info, points, straight_qrcode = qr_code_detector.detectAndDecodeMulti(frame)
    if retval:
        print("QR Code detected!")
        qr_text = decoded_info[0]
        qr_data_list = qr_text.split(',')
        print("QR Code Text:")
        print(qr_text)
        print("Split Data List:")
        print(qr_data_list)
        
        for i in qr_data_list:
            if i=='crocin':
                data_to_send = "crocin"        
            else:
                data_to_send = "NA"
        ser.write(data_to_send.encode())
        
        break

    cv2.imshow('QR Code Scanner', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


const int trigPinC = 2;
const int echoPinC = 3;
const int trigPinC1 = 2;
const int echoPinC1 = 3;
// defines variables
long durationC;
int distanceC;
long durationC1;
int distanceC1;
int disC = 12;
float asin(float c){
	float out;
	out= ((c+(c*c*c)/6+(3*c*c*c*c*c)/40+(5*c*c*c*c*c*c*c)/112+
		(35*c*c*c*c*c*c*c*c*c)/1152 +(c*c*c*c*c*c*c*c*c*c*c*0.022)+
		(c*c*c*c*c*c*c*c*c*c*c*c*c*.0173)+(c*c*c*c*c*c*c*c*c*c*c*c*c*c*c*.0139)+
		(c*c*c*c*c*c*c*c*c*c*c*c*c*c*c*c*c*0.0115)+(c*c*c*c*c*c*c*c*c*c*c*c*c*c*c*c*c*c*c*0.01)
		));
	if(c>=.96 && c<.97){out=1.287+(3.82*(c-.96)); 
}

if(c>=.97 && c<.98){out=(1.325+4.5*(c-.97));} // arcsin
if(c>=.98 && c<.99){out=(1.37+6*(c-.98));}
if(c>=.99 && c<=1){out=(1.43+14*(c-.99));}
return out;
}

float acos(float c)
{
	float out;
	out=asin(sqrt(1-c*c));
	return out;}
	float atan(float c)
	{float out;
		out=asin(c/(sqrt(1+c*c)));
		return out;}


		void setup() {
  // put your setup code here, to run once:
			Serial.begin(9600);
			pinMode(4,OUTPUT);
			pinMode(5,OUTPUT);
//chair strain code
  pinMode(trigPinC, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPinC, INPUT); // Sets the echoPin as an Input
  pinMode(trigPinC1, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPinC1, INPUT); // Sets the echoPin as an Input

}

void loop() {
  // put your main code here, to run repeatedly:
	digitalWrite(5 , HIGH);
	digitalWrite(4 , LOW);
	Serial.println("Dir_1");
	delay(3000);
	digitalWrite(5 , LOW);
	digitalWrite(4 , LOW);


	digitalWrite(trigPinC, LOW);
	delayMicroseconds(2);      
// Sets the trigPin on HIGH state for 10 micro seconds
	digitalWrite(trigPinC, HIGH);
	delayMicroseconds(10);
	digitalWrite(trigPinC, LOW);
// Reads the echoPin, returns the sound wave travel time in microseconds
	durationC = pulseIn(echoPinC, HIGH);
// Calculating the distance
	distanceC= durationC*0.034/2;
// Prints the distance on the Serial Monitor
	Serial.print("Distance: ");
	Serial.print(distanceC);


	Serial.println("Dir_2");
	digitalWrite(4 , HIGH);
	digitalWrite(5 , LOW);
	delay(10000);
	digitalWrite(4 , LOW);
	digitalWrite(5 , LOW);


	digitalWrite(trigPinC1, LOW);
	delayMicroseconds(2);
	digitalWrite(trigPinC1, HIGH);
	delayMicroseconds(10);
	digitalWrite(trigPinC1, LOW);
	durationC1 = pulseIn(echoPinC1, HIGH);
	distanceC1= durationC1*0.034/2;
	Serial.print(" Distance 2: ");
	Serial.print(distanceC1);


	Serial.print(" Angle with Chair : ");

	Serial.println(atan(float(distanceC - distanceC1)/10)*180/3.14);
}
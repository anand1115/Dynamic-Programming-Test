#define t 30
#define t1 20
#define t2 100
#define t3 50

void setup(){
    for(i=2;i<=13;i++){
        pinMode(i,OUTPUT);
    }
}

void loop(){
    event_1();
    event_1();
}

void event_1(){
    for(i=2;i<=13;i++){
        digitalWrite(i,HIGH);
        delay(t1);
        digitalWrite(i+1,HIGH);
        delay(t2);
        digitalWrite(i+2,HIGH);
        delay(t2);
        digitalWrite(i,LOW);
        delay(t2);
        digitalWrite(i+1,LOW);
        delay(t2);
    }
}

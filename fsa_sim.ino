void setup() {
  Serial.begin(9600);

}

int alt=random(0,2);
int lower=0;
int upper=2;

void state(int stateval, String movement, int altitude)
{
    Serial.print("Altitude: ");
    Serial.println(altitude);
    Serial.print("State: ");
    Serial.println(stateval);
    Serial.print("Movement: ");
    Serial.println(movement);
}

void plot_state(int stateval,String movement)
{
}
bool up=true;
void loop() 
{
  if(up)
  {
    alt=random(lower,upper);
    lower=alt;
    upper=lower+30;
  }
  else
  {
    alt=random(lower,upper);
    upper=alt;
    if(upper-30>=0) lower=upper-30;
    else lower=0;

  }
  
  

  // put your main code here, to run repeatedly:
int apogee = 810;
// #state 0 -> ground
// # state 1 -> 0 to 30
// # state 2 - > 30 to apogee
// # state 3-> apogee = 850m
// # rocket deployment, parachute deployment
// # state 3-> apogee to 770m
// # state 4 -> 770 to 500
// # state 5 -> alt <500 
// # deploy secondary parachute
// # state 6 - > 450 to 10
// # state 7 -> alt < 10 ; (landing) ; stop telemetry ; sound buzzer
// # state 8 -> landed


// # to check if state function has been called or not and avoid calling it twice
bool state2done = false; 
bool state3done = false;
bool state4done = false;
bool state5done = false;
bool state6done = false;
bool state7done = false;





    String movement = "ascending";
    int stateval  = 1;


    // alt = data - alt_home;

    if (alt >0 && alt <30 && movement == "ascending")
    {
        stateval = 1;
        state(stateval,movement,alt);
        plot_state(stateval,movement);
    }
    else if (alt >= 30 and alt< apogee and movement == "ascending" && state2done==false)
    {
        stateval = 2;
        state(stateval,movement,alt);
        plot_state(stateval,movement);
        state2done=true;
    }
    else if ((abs(alt-apogee)<30) and movement == "ascending" and state3done == false)
    {
        up=false;
        stateval = 3;
        movement = "descending";
        state(stateval,movement,alt);
        plot_state(stateval,movement);
        state3done = true;
    }
    else if (alt > 770 and movement == "descending")
    {
        stateval = 3;
        state(stateval,movement,alt);
        plot_state(stateval,movement);
    }
   else if (alt > 500 and alt<770 and movement == "descending")
   {
        stateval = 4;
        state(stateval,movement,alt);
        plot_state(stateval,movement);
        state4done=true;
   }
    else if (alt > 450 and alt <=500 and movement == "descending")
    {
        stateval = 5;
        state(stateval,movement,alt);
        plot_state(stateval,movement);
        state5done=true;
    }
   else  if (alt <450 and alt >10 and movement == "descending" && state6done==false)
   {
        stateval = 6;
        state(stateval,movement,alt);
        plot_state(stateval,movement);
        state6done=true;
   }
   else  if (alt <=10 and movement == "landing" && state7done==false)
   {
        stateval = 7;
        state(stateval,movement,alt);
        plot_state(stateval,movement);
        state7done=true;
   }
    else if (alt <0.5 and movement == "landing")
    {
        stateval=8;
        movement = "landed";
        state(stateval,movement,alt);
        plot_state(stateval,movement);
        
    }
 
}

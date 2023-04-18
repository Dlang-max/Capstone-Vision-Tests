import java.util.Scanner; 

public class InverseKinematics
{
    //meters
    private static final double SHOULDER_LENGTH = 0.254; 
    private static final double ELBOW_LENGTH = 0.254; 


    static double x = 0; 
    static double y = 0; 
    static Scanner in = new Scanner( System.in ); 

    public static void main(String[] args)
    {
        System.out.println( "Enter: x:" );
        x = in.nextDouble(); 

        System.out.println( "Enter y:" );
        y = in.nextDouble(); 

        double elbowAngle = Math.acos( ( x * x + y * y - ( SHOULDER_LENGTH * SHOULDER_LENGTH ) - ( ELBOW_LENGTH * ELBOW_LENGTH ) ) / (2 * ELBOW_LENGTH * SHOULDER_LENGTH) );
        double shoulderAngle = Math.atan2( y, x ) - Math.atan2( (ELBOW_LENGTH * Math.sin(elbowAngle)), ( SHOULDER_LENGTH + (ELBOW_LENGTH * Math.cos(elbowAngle ) ) ) );

        elbowAngle = Math.toDegrees( elbowAngle ); 
        shoulderAngle = Math.toDegrees( shoulderAngle ); 

        shoulderAngle = 90 - shoulderAngle; 
        
        System.out.println( "Elbow Angle: " + elbowAngle );
        System.out.println( "Shoulder Angle: " + shoulderAngle );
    }
}
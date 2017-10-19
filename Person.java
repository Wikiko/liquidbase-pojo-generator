public class Person {
    

    private Long id;

    private String firstName;

    private String lastName;

    private String state;

    
    public Person(){
    }
    

    public Long getId(){
        return id;
    }
    
    public void setId(Long id){
        this.id = id;
    }

    public String getFirstname(){
        return firstName;
    }
    
    public void setFirstname(String firstName){
        this.firstName = firstName;
    }

    public String getLastname(){
        return lastName;
    }
    
    public void setLastname(String lastName){
        this.lastName = lastName;
    }

    public String getState(){
        return state;
    }
    
    public void setState(String state){
        this.state = state;
    }


}
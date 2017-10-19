public class Person {
    

    private Long id;

    private String firstname;

    private String lastname;

    private String state;

    
    public Person(){
    }
    

    public Long getId(){
        return id;
    }
    
    public setId(Long id){
        this.id = id;
    }

    public String getFirstname(){
        return firstname;
    }
    
    public setFirstname(String firstname){
        this.firstname = firstname;
    }

    public String getLastname(){
        return lastname;
    }
    
    public setLastname(String lastname){
        this.lastname = lastname;
    }

    public String getState(){
        return state;
    }
    
    public setState(String state){
        this.state = state;
    }


}
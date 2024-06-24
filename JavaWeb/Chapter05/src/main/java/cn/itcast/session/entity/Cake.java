package cn.itcast.session.entity;

public class Cake {
    private static final long serialVersionUID = 1L;



    private String name;
    private String id;
    public Cake() {
    }
    public Cake(String id,String name) {
        this.name = name;
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public String getId() {
        return id;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setId(String id) {
        this.id = id;
    }
}

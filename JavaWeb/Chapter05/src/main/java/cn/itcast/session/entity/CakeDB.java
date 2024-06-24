package cn.itcast.session.entity;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

public class CakeDB {
    private static Map<String, Cake> cakes = new HashMap<String, Cake>();
    static {
        cakes.put("1", new Cake("1", "A蛋糕"));
        cakes.put("2", new Cake("2", "B蛋糕"));
        cakes.put("3", new Cake("3", "C蛋糕"));
        cakes.put("4", new Cake("4", "D蛋糕"));
        cakes.put("5", new Cake("5", "E蛋糕"));
    }
    // 获取所有蛋糕
    public static Collection<Cake> getAll() {
        return cakes.values();
    }
    // 根据id获取蛋糕
    public static Cake getCake(String id) {
        return cakes.get(id);
    }

}

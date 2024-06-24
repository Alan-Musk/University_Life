package com.example.chapter04;

import jakarta.servlet.*;
import jakarta.servlet.http.*;
import jakarta.servlet.annotation.*;

import java.io.IOException;
import java.net.URLDecoder;
import java.net.URLEncoder;
import java.text.SimpleDateFormat;
import java.util.Date;

@WebServlet(name = "LastAccessServlet", value = "/LastAccessServlet")
public class LastAccessServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        // 获取所有的 Cookie
        Cookie[] cookies = request.getCookies();
        // 定义flag的boolean变量，用于判断cookies是否为空
        boolean flag = false;
        // 遍历所有的 Cookie
        if (cookies.length > 0 && cookies != null) {
            for (Cookie cookie : cookies) {
                // 获取cookie的名称
                String name = cookie.getName();
                if ("lastTime".equals(name)) {
                    flag = true;
                    // 获取cookie的值
                    String value = cookie.getValue();
                    System.out.println("解码前：" + value);
                    // URL 解码
                    value = URLDecoder.decode(value, "UTF-8");
                    System.out.println("解码后：" + value);
                    response.getWriter().println("您上次访问的时间是：" + value);
                    // 设置cookie的value
                    // 获取当前时间的字符串，设置为cookie的值
                    Date data = new Date();
                    SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
                    String str_date = sdf.format(data);
                    System.out.println("编码前：" + str_date);
                    // URL 编码
                    str_date = URLEncoder.encode(str_date, "UTF-8");
                    System.out.println("编码后：" + str_date);
                    cookie.setValue(str_date);
                    // 设置cookie的存活时间
                    cookie.setMaxAge(60 * 60 * 24 * 30);
                    response.addCookie(cookie);
                    break;
                }
            }
            // 如果cookies中无时间 就没有访问过
            if(cookies==null || cookies.length==0 || flag==false){
                // 获取当前时间的字符串，设置为cookie的值
                Date data = new Date();
                SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
                String str_date = sdf.format(data);
                System.out.println("编码前：" + str_date);
                // URL 编码
                str_date = URLEncoder.encode(str_date, "UTF-8");
                System.out.println("编码后：" + str_date);
                Cookie cookie = new Cookie("lastTime", str_date);
                // 设置cookie的存活时间
                cookie.setMaxAge(60 * 60 * 24 * 30);
                response.addCookie(cookie);
                response.getWriter().println("您是第一次访问本站！");
            }
        }
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doGet(request,response);
    }
}

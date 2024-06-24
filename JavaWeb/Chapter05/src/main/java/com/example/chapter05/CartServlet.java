package com.example.chapter05;

import cn.itcast.session.entity.Cake;
import jakarta.servlet.*;
import jakarta.servlet.http.*;
import jakarta.servlet.annotation.*;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;

@WebServlet(name = "CartServlet", value = "/CartServlet")
public class CartServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/html;charset=utf-8");
        PrintWriter out = response.getWriter();
        // 获取用户的购物车
        List<Cake> cart=null;
        // 变量purFlag标记用户是否买过商品
        boolean purFlag = true;
        // 获取用户的Session对象
        HttpSession session = request.getSession();
        // 如果Session为null 则purFalag为false
        if(session == null) {
            purFlag = false;
        } else {
            // 获取用户的购物车
            cart = (List<Cake>) session.getAttribute("cart");
            // 如果购物车为null，则purFlag为false
            if(cart == null) {
                purFlag = false;
            }
        }
        // 如果purFlag为false，则提示用户没有购买商品 重定向到ListCakeServlet
        if(!purFlag) {
            out.write("对不起，您没有购买任何商品");
        }else{
            // 显示用户购买的商品
            out.write("您购买的商品有：<br>");
            double price = 0;
            for (Cake cake : cart) {
                out.write(cake.getName()+"<br>");
            }
        }
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doGet(request, response);
    }
}

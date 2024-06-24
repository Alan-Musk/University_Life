package com.example.chapter05;

import cn.itcast.session.entity.Cake;
import cn.itcast.session.entity.CakeDB;
import jakarta.servlet.*;
import jakarta.servlet.http.*;
import jakarta.servlet.annotation.*;

import java.io.IOException;
import java.util.List;

@WebServlet(name = "PurchaseServlet", value = "/PurchaseServlet")
public class PurchaseServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 获取购买的蛋糕id
        String id = request.getParameter("id");
        if (id == null) {
            // 如果ID为null 重定向到ListCakeServlet
            String url = "ListCakeServlet";
            response.sendRedirect(url);
            return;
        }
        Cake cake = CakeDB.getCake(id);
        // 创建或获得用户的Session对象
        HttpSession session = request.getSession();
        // 获取用户的购物车
        List<Cake> cart = (List<Cake>) session.getAttribute("cart");
        if(cart == null) {
            // 如果用户的购物车为null，创建一个购物车
            cart = new java.util.ArrayList<Cake>();
            // 将购物车放入Session对象中
            session.setAttribute("cart", cart);
        }
        // 将蛋糕放入购物车
        cart.add(cake);
        // 创建Cookie存放Session的标示号
        Cookie cookie = new Cookie("JSESSIONID", session.getId());
        cookie.setMaxAge(60*30);
        cookie.setPath("/Servlet");
        response.addCookie(cookie);
        //重定向到购物车页面
        String url = "CartServlet";
        response.sendRedirect(url);
    }
}

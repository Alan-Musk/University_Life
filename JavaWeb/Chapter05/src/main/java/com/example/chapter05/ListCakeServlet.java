package com.example.chapter05;

import cn.itcast.session.entity.Cake;
import cn.itcast.session.entity.CakeDB;
import jakarta.servlet.*;
import jakarta.servlet.http.*;
import jakarta.servlet.annotation.*;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.Collection;

@WebServlet(name = "ListCakeServlet", value = "/ListCakeServlet")
public class ListCakeServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/html;charset=utf-8");
        PrintWriter out = response.getWriter();
        Collection<Cake> cakes = CakeDB.getAll();
        out.write("当前系统中存在的蛋糕有：<br>");
        for (Cake cake : cakes) {
            String url="PurchaseServlet?id="+cake.getId();
            out.write(cake.getName()+"<a href='"+url+"'>购买</a><br>");
        }
    }
}

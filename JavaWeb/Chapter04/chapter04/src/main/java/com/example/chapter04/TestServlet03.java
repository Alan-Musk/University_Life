package com.example.chapter04;

import jakarta.servlet.*;
import jakarta.servlet.http.*;
import jakarta.servlet.annotation.*;

import java.io.IOException;
import java.io.PrintWriter;

@WebServlet(name = "TestServlet03", value = "/TestServlet03",initParams = {@WebInitParam(name= "encoding", value = "UTF-8")})
public class TestServlet03 extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        PrintWriter out = response.getWriter();
        // 获取ServletConfig对象
        ServletConfig config = this.getServletConfig();
        // 获取初始化参数
        String encoding = config.getInitParameter("encoding");
        out.println("encoding: " + encoding);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        this.doGet(request, response);
    }
}

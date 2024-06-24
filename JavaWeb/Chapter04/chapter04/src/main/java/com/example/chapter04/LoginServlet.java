package com.example.chapter04;

import jakarta.servlet.*;
import jakarta.servlet.http.*;
import jakarta.servlet.annotation.*;

import java.io.IOException;
import java.io.PrintWriter;

@WebServlet(name = "LoginServlet", value = "/LoginServlet")
public class LoginServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        // 使用HttpServletRequest对象的getParameter()方法获取请求参数
        String username = request.getParameter("username");
        String password = request.getParameter("password");
        PrintWriter out = response.getWriter();
        out.println("用户名：" + username + "<br>");
        out.println("密码：" + password + "<br>");
        // 假设用户名和密码分别为admin和123456
        if ("admin".equals(username) && "123456".equals(password)) {
            // 登录成功，重定向到success.html
            response.sendRedirect("welcome.html");
        } else {
            // 登录失败，重定向到fail.html
            response.sendRedirect("fail.html");
        }
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doGet(request, response);
    }
}

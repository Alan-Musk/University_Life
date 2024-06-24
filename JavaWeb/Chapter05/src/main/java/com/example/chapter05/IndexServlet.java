package com.example.chapter05;

import cn.itcast.session.entity.User;
import jakarta.servlet.*;
import jakarta.servlet.http.*;
import jakarta.servlet.annotation.*;

import java.io.IOException;


@WebServlet(name = "IndexServlet", value = "/IndexServlet")
public class IndexServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
            response.setContentType("text/html;charset=utf-8");
            HttpSession session = request.getSession();
            User user = (User) session.getAttribute("user");
            if(user == null){
                response.getWriter().write("您还没有登录，请<a href='/chapter05/login.html'>登录</a>");
            }
            else {
                response.getWriter().write("欢迎您，" + user.getUsername() + "，<a href='/chapter05/LogoutServlet'>退出</a>");
                // 创建Cookie，存放Session1的标示号
                Cookie cookie = new Cookie("JSESSIONID", session.getId());
                cookie.setMaxAge(60 * 30);
                cookie.setPath("/chapter05");
                response.addCookie(cookie);
            }
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doGet(request, response);
    }
}

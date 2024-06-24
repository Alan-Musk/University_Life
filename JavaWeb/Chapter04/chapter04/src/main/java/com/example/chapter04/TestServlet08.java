package com.example.chapter04;

import jakarta.servlet.*;
import jakarta.servlet.http.*;
import jakarta.servlet.annotation.*;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Properties;

@WebServlet(name = "TestServlet08", value = "/TestServlet08")
public class TestServlet08 extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
            response.setContentType("text/html;charset=UTF-8");
            PrintWriter out = response.getWriter();
            ServletContext context = this.getServletContext();
            // 获取文件绝对路径
            String path = context.getRealPath("/WEB-INF/classes/itcast.properties");
            FileInputStream fis = new FileInputStream(path);
            Properties pros = new Properties();
            pros.load(fis);
            out.println("Company=" + pros.getProperty("Company") + "<br>");
            out.println("Address=" + pros.getProperty("Address") + "<br>");
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doGet(request, response);
    }
}

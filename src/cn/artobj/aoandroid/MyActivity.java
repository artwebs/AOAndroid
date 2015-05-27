package cn.artobj.aoandroid;

import android.app.Activity;
import android.app.AlertDialog;
import android.os.Bundle;
import cn.artobj.android.app.AlertStyle;

public class MyActivity extends Activity {
    /**
     * Called when the activity is first created.
     */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        new AlertDialog.Builder(this)
                .setIcon(AlertStyle.info.getIco())
                .setTitle(AlertStyle.info.getTitle())
                .setMessage("测试")
                .setNegativeButton("确定",null)
                .show();

    }
}

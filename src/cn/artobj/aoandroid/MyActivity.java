package cn.artobj.aoandroid;

import android.app.Activity;
import android.os.Bundle;
import cn.artobj.android.application.AppApplication;

public class MyActivity extends Activity {
    /**
     * Called when the activity is first created.
     */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
    }
}

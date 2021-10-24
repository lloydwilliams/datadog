package com.example.mobileandroid

import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import androidx.appcompat.app.AppCompatActivity
import androidx.navigation.findNavController
import androidx.navigation.ui.AppBarConfiguration
import androidx.navigation.ui.navigateUp
import androidx.navigation.ui.setupActionBarWithNavController
import com.datadog.android.Datadog
import com.datadog.android.core.configuration.Configuration
import com.datadog.android.core.configuration.Credentials
import com.datadog.android.privacy.TrackingConsent
import com.datadog.android.rum.GlobalRum
import com.datadog.android.rum.RumMonitor
import com.example.mobileandroid.databinding.ActivityMainBinding
import com.google.android.material.snackbar.Snackbar

class MainActivity : AppCompatActivity() {

    private lateinit var appBarConfiguration: AppBarConfiguration
    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        //Datadog
        val clientToken = "<<USE YOUR OWN CLIENT TOKEN>>"
        val applicationId = "<<USE YOUR OWN APPLICATION ID>>"

        val environmentName = "dev"
        val appVariantName = "myAppVariantName"

        val durationThreshold = 300L
        //val trackingStrategy = TrackingStrategy.ActivityViewTrackingStrategy
        //.useViewTrackingStrategy(trackingStrategy)
        val trackingConsent = TrackingConsent.GRANTED


        val configuration = Configuration.Builder(
            rumEnabled = true,
            crashReportsEnabled = true,
            logsEnabled = true,
            tracesEnabled = true
        )
            .trackInteractions()
            .trackLongTasks(durationThreshold)
            .build()
        val credentials = Credentials(clientToken,environmentName,appVariantName,applicationId)

        Datadog.initialize(this, credentials, configuration, trackingConsent)
        GlobalRum.registerIfAbsent(RumMonitor.Builder().build())

        //End Datadog

        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        setSupportActionBar(binding.toolbar)

        val navController = findNavController(R.id.nav_host_fragment_content_main)
        appBarConfiguration = AppBarConfiguration(navController.graph)
        setupActionBarWithNavController(navController, appBarConfiguration)

        binding.fab.setOnClickListener { view ->
            Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                    .setAction("Action", null).show()
        }
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        // Inflate the menu; this adds items to the action bar if it is present.
        menuInflater.inflate(R.menu.menu_main, menu)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        return when (item.itemId) {
            R.id.action_settings -> true
            else -> super.onOptionsItemSelected(item)
        }
    }

    override fun onSupportNavigateUp(): Boolean {
        val navController = findNavController(R.id.nav_host_fragment_content_main)
        return navController.navigateUp(appBarConfiguration)
                || super.onSupportNavigateUp()
    }
}